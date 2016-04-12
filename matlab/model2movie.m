function v = model2movie(g,gbar,E,V,slowdown)
%slowdown is the decimation factor
v = VideoWriter('Spike2.avi')
v.FrameRate = 30
open(v)
%upper bound for radius - needs to be held constant
%since size of sqrt(V) changes each frame
VBOUND = 130
for i = 1:slowdown:length(V)
    msdiagram(g(:,i),gbar(:,i),E(:,i),V(i))
    xlim(sqrt(VBOUND)*[-1 1])
    ylim(sqrt(VBOUND)*[-1 1])
    F = getframe(gca)
    close
    writeVideo(v,F)
end
close(v)
end
