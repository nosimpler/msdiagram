% Author: Robert Law
% Date: October 13, 2015
% msdiagram: Conductance model visualization 
% Takes conductances, maximal conductances, reversal potentials, and
% voltage, and plots geometrically according to Law and Levin (2015)
% and Law and Jones (in preparation)

function h = msdiagram(gbar, p, E, V)
% if MINSHIFT == 0, abs(lowest reversal) will be used
% as V_shift. Otherwise add the value of MINSHIFT
% to abs(lowest reversal) to V_shift
MINSHIFT = 1
%G is the conductance if all channels of all types were open
G = sum(gbar)
%p is fraction of open channels in each channel population 
%convert gbar to a fraction of the circle
gbar_angle = 2*pi*gbar/G

%bounding angles dividing cell into gbar-proportional components
lb_gbar_angle = [0;cumsum(gbar_angle)]

%conductance angles grow from center
center_angle = (lb_gbar_angle(2:end)+lb_gbar_angle(1:end-1))/2

%bounding angles for each current
l_angle = center_angle + gbar_angle.*p/2
r_angle = center_angle - gbar_angle.*p/2

%intermediate angles for constructing a patch
for i = 1:length(l_angle)
    patch_angle(i,:) = linspace(r_angle(i),l_angle(i),50) 
end

%shift voltages if necessary
if all(E > 0) & all(V > 0)
    
else
    shift = abs(min([V;E]))
    V = V + shift + MINSHIFT
    E = E + shift + MINSHIFT
end

%get radii
for i = 1:length(E)
    if E(i)>V
        R(i) = sqrt(E(i))
        r(i) = sqrt(V)
    else
        R(i) = sqrt(V)
        r(i) = sqrt(E(i))
    end
end

%construct patches
for i = 1:length(l_angle)
    xmin = r(i)*cos(patch_angle(i,:))
    xmax = R(i)*cos(patch_angle(i,end:-1:1))
    ymin = r(i)*sin(patch_angle(i,:))
    ymax = R(i)*sin(patch_angle(i,end:-1:1))
    X(i,:) = [xmin xmax]
    Y(i,:) = [ymin ymax]
end
circ_theta = 0:0.005:2*pi;
circ_rho = sqrt(V)*ones(1,length(circ_theta));

figure
hold all
% sqrt(V) circular 'cell'
h = polar(circ_theta, circ_rho, 'k')
set(h,'LineWidth', 2)

%color patches represent currents
co = [0    0.4470    0.7410;
      0.8500    0.3250    0.0980;
      0.9290    0.6940    0.1250;
      0.4940    0.1840    0.5560;
      0.4660    0.6740    0.1880;
      0.3010    0.7450    0.9330;
      0.6350    0.0780    0.1840]
for i = 1:length(l_angle)
    %borders same color 
    %patch(X(i,:)',Y(i,:)', co(i,:),'EdgeColor', co(i,:))
    %borders white
    patch(X(i,:)',Y(i,:)', co(i,:),'EdgeColor', 'w')
end



%draw lines between different channel populations
%don't draw if only one channel type
if length(gbar) > 1
    for i = 1:length(gbar)
        line_rho = [0; sqrt(V)]
        line_theta = [lb_gbar_angle(i); lb_gbar_angle(i)]
        polar(line_theta,line_rho,'k')
        set(h,'LineWidth',1)
    end
end
hold off
end
