/********************
Modified NL means filter for B1 correction

Michael Eager
Zhaolin Chen
Monash Biomedical Imaging

Monash University, 2015
 *******************/


/***************************************************************************/
/* Jose V. Manjon - jmanjon@fis.upv.es                                     */
/* Universidad Politecnica de Valencia, Spain                              */
/* Pierrick Coupe - pierrick.coupe@gmail.com                               */
/* Brain Imaging Center, Montreal Neurological Institute.                  */
/* Mc Gill University                                                      */
/*                                                                         */
/* Copyright (C) 2010 Jose V. Manjon and Pierrick Coupe                    */

/***************************************************************************
 * New Methods for MRI Denoising based on Sparseness and Self-Similarity    *
 * Jos� V. Manj�n, Pierrick Coup�, Antonio Buades,D. Louis Collins
 * and Montserrat Robles
 ***************************************************************************/

#include "math.h"
#include "mex.h"
#include <stdlib.h>
#include <stdio.h>
#include "matrix.h"

/* Multithreading stuff*/
#ifdef _WIN32
#include <windows.h>
#include <process.h>
#else
#include <pthread.h>
#endif

#define max(x,y) x < y ? y : x
#define min(x,y) x > y ? y : x
enum gamma_kernel_method {GAMMAMINMAX = 0, GAMMAMULT, GAMMADR, GAMMAEXPDR, GAMMADIFF};

int GAMMAfunction = 0;

typedef struct {
    int rows;
    int cols;
    int slices;
    float * in_image;
    float * out_image;
    float * means_image;
    float * ref_image;
    float * pesos;  //spanish for pound or weight
    float * coilsens_image;
    int ini;
    int fin;
    int radioB; //radius of patch area
    int radioS; //radius of search area
    float sigma;
    int order;

} myargument;

bool rician;

void* ThreadFunc(void* pArguments)
{
    float *ima, *fima, *medias, *pesos, *ref, *coilsens;
    float sigma, w, d, hhh, hh, t1, alfa, x, gamma, epsilon;
    int ii, jj, kk, ni, nj, nk, i, j, k, ini, fin, rows, cols, slices, p, p1, radioS, radioB, order, rc;
    extern bool rician;
    /*extern float *table;*/

    myargument arg;
    arg = *(myargument *) pArguments;

    rows = arg.rows;
    cols = arg.cols;
    slices = arg.slices;
    ini = arg.ini;
    fin = arg.fin;
    ima = arg.in_image;
    fima = arg.out_image;
    medias = arg.means_image;
    ref = arg.ref_image;
    coilsens = arg.coilsens_image;
    pesos = arg.pesos;
    radioB = arg.radioB;
    radioS = arg.radioS;
    sigma = arg.sigma;
    order = arg.order;
    epsilon = 0.00001;
    hh = 2 * sigma * sigma;
    alfa = 0.5;
    hhh = 0.5 * sigma * sigma;
    rc = rows * cols;

    /* filter*/

    if (order == 1)
    {
        for (k = ini; k < fin; k++)
        {
            for (j = 0; j < rows; j++)
            {
                for (i = 0; i < cols; i++)
                {
                    p = k * rc + j * cols + i;

                    if (ima[p] == 0) continue;

                    for (kk = 0; kk <= radioB; kk++)
                    {
                        nk = k + kk;
                        for (jj = -radioB; jj <= radioB; jj++)
                        {
                            nj = j + jj;
                            for (ii = -radioB; ii <= radioB; ii++)
                            {
                                ni = i + ii;
                                if (kk == 0 && jj < 0) continue;
                                if (kk == 0 && jj == 0 && ii <= 0) continue;

                                if (ni >= 0 && nj >= 0 && nk >= 0 && ni < cols && nj < rows && nk < slices)
                                {
                                    p1 = nk * rc + nj * cols + ni;
                                    if (GAMMAfunction == GAMMAMULT) {
                                        t1 = fabs(medias[p] / coilsens[p] - medias[p1] / coilsens[p1]);
                                        if (t1 > sigma) continue;
                                        w = (ref[p] / coilsens[p] - ref[p1] / coilsens[p1]);
                                        w = (w * w) / hh - 1;
                                        d = (t1 * t1) / hhh - 1;

                                        w = w < 0 ? 0 : w;
                                        d = d < 0 ? 0 : d;

                                        d = w * 0.5 + d * 0.5;
                                    }
                                    else {

                                        t1 = abs(medias[p] - medias[p1]);
                                        if (t1 > sigma) continue;
                                        w = (ref[p] - ref[p1]);

                                        w = (w * w) / hh - 1;
                                        d = (t1 * t1) / hhh - 1;

                                        w = w < 0 ? 0 : w;
                                        d = d < 0 ? 0 : d;

                                        d = w * 0.5 + d * 0.5;
                                        if (GAMMAfunction == GAMMAMINMAX) {
                                            // Eager ammendment:
                                            // Coil sensitivity (B1) correction
                                            // adjust weight factor d by beta^2, where
                                            // beta is the difference between approx.
                                            // B1 values at p and p1. Coil sensitivity
                                            // gives the approx B1 image.
                                            //                                    gamma = (coilsens[p]-coilsens[p1]);
                                            gamma = max(coilsens[p], coilsens[p1]) / min(coilsens[p], coilsens[p1]);
                                            if (gamma > 0) d *= 1 / (gamma * gamma);
                                            //

                                        }
                                        else if (GAMMAfunction == GAMMADR) {
                                            // Exponential DR method
                                            gamma = 1 + (fabs(coilsens[p] - coilsens[p1]));
                                            if (gamma != 0) d *= 1 / (gamma * gamma);
                                        }
                                        else if (GAMMAfunction == GAMMAEXPDR) {
                                            // Exponential DR method
                                            gamma = exp(fabs(coilsens[p] - coilsens[p1]));
                                            if (gamma != 0) d *= 1 / (gamma * gamma);

                                        }
                                        else if (GAMMAfunction == GAMMADIFF) {
                                            gamma = (coilsens[p] - coilsens[p1]);
                                            if (gamma != 0) d *= 1 / (gamma * gamma);
                                        }
                                    }

                                    if (d <= 0) w = 1.0;
                                    else if (d > 10) w = 0;
                                    else w = exp(-d);

                                    if (rician > 0)
                                    {
                                        fima[p] += w * ima[p1] * ima[p1];
                                        pesos[p] += w;

                                        fima[p1] += w * ima[p] * ima[p];
                                        pesos[p1] += w;
                                    }
                                    else
                                    {
                                        fima[p] += w * ima[p1];
                                        pesos[p] += w;

                                        fima[p1] += w * ima[p];
                                        pesos[p1] += w;
                                    }

                                }
                            }
                        }
                    }
                }
            }
        }

    }
    else
    {
        for (k = ini; k < fin; k++)
        {
            for (j = rows - 1; j >= 0; j--)
            {
                for (i = cols - 1; i >= 0; i--)
                {
                    p = k * rc + j * cols + i;
                    if (ima[p] == 0) continue;

                    for (kk = 0; kk <= radioB; kk++)
                    {
                        nk = k + kk;
                        for (jj = -radioB; jj <= radioB; jj++)
                        {
                            nj = j + jj;
                            for (ii = -radioB; ii <= radioB; ii++)
                            {
                                ni = i + ii;
                                if (kk == 0 && jj < 0) continue;
                                if (kk == 0 && jj == 0 && ii <= 0) continue;

                                if (ni >= 0 && nj >= 0 && nk >= 0 && ni < cols && nj < rows && nk < slices)
                                {
                                    p1 = nk * rc + nj * cols + ni;

                                    if (GAMMAfunction == GAMMAMULT) {
                                        t1 = abs(medias[p] / coilsens[p] - medias[p1] / coilsens[p1]);
                                        if (t1 > sigma) continue;
                                        w = (ref[p] / coilsens[p] - ref[p1] / coilsens[p1]);

#ifdef FP_FAST_FMA
                                        w = fma(w * w, 1.0f / h, -1);
                                        d = fma(t1 * t1, 1, 0f / hhh, -1);
#else
                                        w = (w * w) / hh - 1;
                                        d = (t1 * t1) / hhh - 1;
#endif
                                        w = w < 0 ? 0 : w;
                                        d = d < 0 ? 0 : d;

                                        d = w * 0.5 + d * 0.5;
                                    }
                                    else {


                                        t1 = abs(medias[p] - medias[p1]);
                                        if (t1 > sigma) continue;

                                        w = (ref[p] - ref[p1]);
#ifdef FP_FAST_FMA
                                        w = fma(w * w, 1.0f / h, -1);
                                        d = fma(t1 * t1, 1, 0f / hhh, -1);
#else
                                        w = (w * w) / hh - 1;
                                        d = (t1 * t1) / hhh - 1;
#endif
                                        w = w < 0 ? 0 : w;
                                        d = d < 0 ? 0 : d;

                                        d = w * 0.5 + d * 0.5;

                                        if (GAMMAfunction == GAMMAMINMAX) {
                                            //Coil sensitivity (B1) correction
                                            gamma = max(coilsens[p], coilsens[p1]) / min(coilsens[p], coilsens[p1]);
                                            if (gamma != 0) d *= 1 / (gamma * gamma);

                                        }
                                        else if (GAMMAfunction == GAMMADR) {
                                            // Exponential DR method
                                            gamma = 1 + (fabs(coilsens[p] - coilsens[p1]));
                                            if (gamma > 2 * epsilon) d *= 1 / (gamma * gamma);
                                        }
                                        else if (GAMMAfunction == GAMMAEXPDR) {
                                            // Exponential DR method
                                            gamma = exp(fabs(coilsens[p] - coilsens[p1]));
                                            if (gamma > 2 * epsilon) d *= 1 / (gamma * gamma);
                                        }
                                        else if (GAMMAfunction == GAMMADIFF) {
                                            gamma = fabs(coilsens[p] - coilsens[p1]);
                                            if (gamma > epsilon) d *= 1 / (gamma);
                                        }
                                    }
                                    if (d <= 0) w = 1.0;
                                    else if (d > 10) w = 0;
                                    else w = exp(-d);
                                    pesos[p1] += w;
                                    pesos[p] += w;

                                    if (rician > 0)
                                    {
#ifdef FP_FAST_FMA
                                        fima[p] = fma(w, ima[p1] * ima[p1], fima[p]);
                                        fima[p] = fma(w, ima[p] * ima[p], fima[p1]);
#else
                                        fima[p] += w * ima[p1] * ima[p1];

                                        fima[p1] += w * ima[p] * ima[p];
#endif
                                    }
                                    else
                                    {
#ifdef FP_FAST_FMA
                                        fima[p] = fma(w, ima[p1], fima[p]);
                                        fima[p] = fma(w, ima[p], fima[p1]);

#else
                                        fima[p] += w * ima[p1];

                                        fima[p1] += w * ima[p];
#endif
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

#ifdef _WIN32
    _endthreadex(0);
#else
    pthread_exit(0);
#endif

    return 0;
}

void mexFunction(int nlhs, mxArray *plhs[], int nrhs, const mxArray *prhs[])
{
    /*Declarations*/
    mxArray *xData, *pv, *Mxmedias, *Mxpesos, *xref, *MxCoil;
    float *ima, *fima, *lista, *pesos, *ref, *medias, *coilsens;
    float sigma, vr, R, h, w, average, totalweight, wmax, d, media, var, th, hh, hhh, wm, t1, t2, alfa;
    int Ndims, inc, i, j, k, ii, jj, kk, ni, nj, nk, radioB, radioS,  indice, Nthreads, ini, fin, order;
    int ndim;
    const int  *dims, *coildims;

    myargument *ThreadArgs;

#ifdef _WIN32
    HANDLE *ThreadList; /* Handles to the worker threads*/
#else
    pthread_t * ThreadList;
#endif
    mexPrintf("myRINLM: Start mex function \n");
    mexEvalString("drawnow");
    if (nrhs < 6 || nrhs > 8)
    {
        mexErrMsgIdAndTxt("myRINLM3D: Not enough arguments \n",
                          "Usage: OutputImage=myRINLM3D(InputImage,searcharea,patcharea,sigma,ODCTImage,rician,CoilSensitivityImage[,GAMMAfunction]) ");
        // exit MEX-file
    }

    /*Copy input pointer x*/
    mexPrintf("myRINLM: Get input image \n");
    /*Get matrix x*/
    if (mxIsSparse(prhs[0]) ||
            mxIsComplex(prhs[0]) ||
            mxIsDouble(prhs[0])  ||
            mxGetNumberOfElements(prhs[0]) == 1 ||
            mxGetNumberOfDimensions(prhs[0]) != 3) {
        mexErrMsgIdAndTxt("myRINLM3d:InputImage", " input1 must be full matrix of real float values.");
    }
    ima = (float*)mxGetPr(prhs[0]);
    ndim = mxGetNumberOfDimensions(prhs[0]);
    dims = mxGetDimensions(prhs[0]);
    mexPrintf("myRINLM: Get params \n");
    /*Copy input parameters*/
    /*Get the search area*/
    if (mxIsComplex(prhs[1]) ||
            mxGetNumberOfElements(prhs[1]) != 1) {
        mexErrMsgIdAndTxt("myRINLM3d:Searcharea", " search area must be an integer.");
        return ;
    }
    radioS = (int)(mxGetScalar(prhs[1]));

    if (mxIsComplex(prhs[2]) ||
            mxGetNumberOfElements(prhs[2]) != 1) {
        mexErrMsgIdAndTxt("myRINLM3d:Patchsize", " patch area must be an integer.");
    }
    radioB = (int)(mxGetScalar(prhs[2]));

    if (mxIsSparse(prhs[3]) ||
            mxIsComplex(prhs[3]) ||
            mxGetNumberOfElements(prhs[3]) != 1) {
        mexErrMsgIdAndTxt("myRINLM3d:Sigma", " sigma must be real value.");
    }
    sigma = (float)(mxGetScalar(prhs[3]));

    if (mxIsSparse(prhs[4]) ||
            mxIsComplex(prhs[4]) ||
            mxIsDouble(prhs[4])  ||
            mxGetNumberOfElements(prhs[4]) == 1 ||
            mxGetNumberOfDimensions(prhs[4]) != 3) {
        mexErrMsgIdAndTxt("myRINLM3d:RefImage", " ref must be full matrix of real float values.");
        return;
    }
    ref = (float*)mxGetPr(prhs[4]);

    if (mxIsSparse(prhs[5]) ||
            mxIsComplex(prhs[5]) ||
            mxGetNumberOfElements(prhs[5]) != 1) {
        mexErrMsgIdAndTxt("myRINLM3d:RicianFlag", " rician must be real value or bool.");
    }
    rician = (int)(mxGetScalar(prhs[5]));

    h = sigma / 3.0f; /* this is due to the removal of part of the noise*/
    mexPrintf("myRINLM: H %f\n", h);
    if (nrhs >= 7)
    {
        if (mxIsSparse(prhs[6]) ||
                mxIsComplex(prhs[6]) ||
                mxIsDouble(prhs[6])  ||
                mxGetNumberOfElements(prhs[6]) == 1 ||
                mxGetNumberOfDimensions(prhs[6]) != 3) {
            mexErrMsgIdAndTxt("myRINLM3d:B1CoilSensImage", " B1 coil sens must be full matrix of real float values.");
            return;
        }
        coildims = mxGetDimensions(prhs[6]);
        if (coildims[0] != dims[0] || coildims[1] != dims[1] || coildims[2] != dims[2])
        {
            mexErrMsgIdAndTxt("myMBONLM:B1CoilSensImage", " coil dims must equal input image dims.");
            return;
        }
        coilsens = (float*)mxGetPr(prhs[6]);
    }
    else
    {
        pv = mxCreateNumericArray(ndim, dims, mxSINGLE_CLASS, mxREAL);
        coilsens = (float*)mxGetPr(pv);
        for (k = 0; k < dims[2]*dims[1]*dims[0]; k++)
            coilsens[i] = 1.0;
    }
    if (nrhs == 8)
    {
        if (mxIsSparse(prhs[7]) ||
                mxIsComplex(prhs[7]) ||
                mxGetNumberOfElements(prhs[7]) != 1) {
            mexErrMsgIdAndTxt("myMBONLM:GAMMAfunction", " GAMMA function flag must be an integer between 0 and 4.");
        }
        GAMMAfunction = (int)(mxGetScalar(prhs[7]));

        switch (GAMMAfunction) {
        case GAMMAMULT:
            GAMMAfunction = GAMMAMULT;
            mexPrintf("myRINLM: GAMMAfunction set to GAMMAMULT.\n"); break;
        case GAMMADR:
            GAMMAfunction = GAMMADR;
            mexPrintf("myRINLM: GAMMAfunction set to GAMMADR.\n"); break;
        case GAMMAEXPDR:
            GAMMAfunction = GAMMAEXPDR;
            mexPrintf("myRINLM: GAMMAfunction set to GAMMAEXPDR.\n"); break;
        case GAMMADIFF:
            GAMMAfunction = GAMMADIFF;
            mexPrintf("myRINLM: GAMMAfunction set to GAMMADIFF.\n"); break;
        otherwise:
            GAMMAfunction = GAMMAMINMAX;
            mexPrintf("myRINLM: GAMMAfunction set to default GAMMAMINMAX.\n");
        }
    }
    else {
        GAMMAfunction = GAMMAMINMAX;
        mexPrintf("myRINLM: GAMMAfunction set to default (GAMMAMINMAX).\n");
    }

    mexPrintf("myRINLM: Creating output matricies \n");
    /* Allocate memory and assign output pointer */
    /* Get a pointer to the data space in our newly allocated memory */
    plhs[0] = mxCreateNumericArray(ndim, dims, mxSINGLE_CLASS, mxREAL);
    fima = (float*) mxGetPr(plhs[0]);
    if (nlhs > 1)
    {
        plhs[1] = mxCreateNumericArray(ndim, dims, mxSINGLE_CLASS, mxREAL);
        medias = (float*) mxGetPr(plhs[1]);
    }
    else
    {
        Mxmedias = mxCreateNumericArray(ndim, dims, mxSINGLE_CLASS, mxREAL);
        medias = (float*) mxGetPr(Mxmedias);
    }
    if (nlhs > 2)
    {
        plhs[2]  = mxCreateNumericArray(ndim, dims, mxSINGLE_CLASS, mxREAL);
        pesos = (float*) mxGetPr(plhs[2]);
    }
    else
    {
        Mxpesos = mxCreateNumericArray(ndim, dims, mxSINGLE_CLASS, mxREAL);
        pesos = (float*) mxGetPr(Mxpesos);
    }

    mexPrintf("myRINLM: Calculating means \n");
    /* calculate means*/
    int indx;
    for (k = 0; k < dims[2]; k++)
    {
        for (j = 0; j < dims[1]; j++)
        {
            for (i = 0; i < dims[0]; i++)
            {
                indx = k * (dims[0] * dims[1]) + (j * dims[0]) + i;
                media = ref[indx];
                for (ii = -1; ii <= 1; ii++)
                {
                    ni = i + ii;
                    if (ni < 0) ni = -ni;
                    if (ni >= dims[0]) ni = 2 * dims[0] - ni - 1;
                    for (jj = -1; jj <= 1; jj++)
                    {
                        nj = j + jj;
                        if (nj < 0) nj = -nj;
                        if (nj >= dims[1]) nj = 2 * dims[1] - nj - 1;
                        for (kk = -1; kk <= 1; kk++)
                        {
                            nk = k + kk;
                            if (nk < 0) nk = -nk;
                            if (nk >= dims[2]) nk = 2 * dims[2] - nk - 1;

                            if (sqrt(ii * ii + jj * jj + kk * kk) > 1)continue;
                            indx = nk * (dims[0] * dims[1]) + (nj * dims[0]) + ni ;
                            media = media + ref[indx];
                        }
                    }
                }
                media = media / 8;
                medias[k * (dims[0]*dims[1]) + (j * dims[0]) + i] = media;
            }
        }
    }

    for (k = 0; k < dims[2]*dims[1]*dims[0]; k++)
    {
        if (rician > 0) fima[k] = ima[k] * ima[k];
        else fima[k] = ima[k];
        pesos[k] = 1.0;
    }

    Nthreads = dims[2] < 24 ? dims[2] : 24;
    if (Nthreads < 1) Nthreads = 1;
#ifdef _WIN32

    /* Reserve room for handles of threads in ThreadList*/
    ThreadList = (HANDLE*)malloc(Nthreads * sizeof(HANDLE));
    ThreadArgs = (myargument*) malloc(Nthreads * sizeof(myargument));

    order = -1;
    for (i = 0; i < Nthreads; i++)
    {
        /* Make Thread Structure*/
        order = -order;
        ini = (i * dims[2]) / Nthreads;
        fin = ((i + 1) * dims[2]) / Nthreads;
        ThreadArgs[i].cols = dims[0];
        ThreadArgs[i].rows = dims[1];
        ThreadArgs[i].slices = dims[2];
        ThreadArgs[i].in_image = ima;
        ThreadArgs[i].out_image = fima;
        ThreadArgs[i].ref_image = ref;
        ThreadArgs[i].means_image = medias;
        ThreadArgs[i].coilsens_image = coilsens;
        ThreadArgs[i].pesos = pesos;
        ThreadArgs[i].ini = ini;
        ThreadArgs[i].fin = fin;
        ThreadArgs[i].radioB = radioB;
        ThreadArgs[i].radioS = radioS;
        ThreadArgs[i].sigma = h;
        ThreadArgs[i].order = order;

        ThreadList[i] = (HANDLE)_beginthreadex(NULL, 0, &ThreadFunc, &ThreadArgs[i] , 0, NULL);

    }

    for (i = 0; i < Nthreads; i++) {
        WaitForSingleObject(ThreadList[i], INFINITE);
    }
    for (i = 0; i < Nthreads; i++) {
        CloseHandle(ThreadList[i]);
    }


#else

    mexPrintf("myRINLM3D: Pthreading %d\n", Nthreads);
    /* Reserve room for handles of threads in ThreadList*/
    ThreadList = (pthread_t *) calloc(Nthreads, sizeof(pthread_t));
    ThreadArgs = (myargument*) calloc(Nthreads, sizeof(myargument));

    order = -1;
    for (i = 0; i < Nthreads; i++)
    {
        /* Make Thread Structure*/
        order = -order;
        ini = (i * dims[2]) / Nthreads;
        fin = ((i + 1) * dims[2]) / Nthreads;
        ThreadArgs[i].cols = dims[0];
        ThreadArgs[i].rows = dims[1];
        ThreadArgs[i].slices = dims[2];
        ThreadArgs[i].in_image = ima;
        ThreadArgs[i].out_image = fima;
        ThreadArgs[i].ref_image = ref;
        ThreadArgs[i].means_image = medias;
        ThreadArgs[i].coilsens_image = coilsens;
        ThreadArgs[i].pesos = pesos;
        ThreadArgs[i].ini = ini;
        ThreadArgs[i].fin = fin;
        ThreadArgs[i].radioB = radioB;
        ThreadArgs[i].radioS = radioS;
        ThreadArgs[i].sigma = h;
        ThreadArgs[i].order = order;
    }
    mexPrintf("myRINLM: Starting threads \n");
    for (i = 0; i < Nthreads; i++)
    {
        if (pthread_create(&ThreadList[i], NULL, ThreadFunc, &ThreadArgs[i]))
        {
            printf("Threads cannot be created\n");
            return;
        }
    }

    for (i = 0; i < Nthreads; i++)
    {
        pthread_join(ThreadList[i], NULL);
    }
#endif

    mexPrintf("myRINLM: Threads completed \n");

    free(ThreadArgs);
    free(ThreadList);


    sigma = 2 * sigma * sigma;
    for (k = 0; k < dims[2]*dims[1]*dims[0]; k++)
    {
        if (rician > 0)
        {
#ifdef FP_FAST_FMA
            vr = fma(fima[k], 1.0f / pesos[k], -sigma);
#else
            vr = (fima[k] / pesos[k]) - sigma;
#endif
            if (vr < 0) fima[k] = 0;
            else fima[k] = sqrt(vr);
            if (ima[k] <= 0) fima[k] = 0;
        }
        else fima[k] /= pesos[k];
    }
    mexPrintf("myRINLM3D: done \n");
    return;


}

