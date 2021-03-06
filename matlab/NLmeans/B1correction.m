function b1=B1correction(img,verbose)
%% DCT and B1 correction

% large scale local structure effects
%
% not to be used on body coil images
%
% 5th order best
b1=zeros(size(b1));
for slice = 1:size(img,3)
    dcts = dct2(img(:,:,slice)); 
    dctt = zeros(size(dcts)); 
    nn=5; 
    dctt(1:nn,1:nn) = dcts(1:nn,1:nn); 
    b1(:,:,slice) = idct2(dctt); 
end
if (nargin == 2)
    figure; imagesc(b1)
end
