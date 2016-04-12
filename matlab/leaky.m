function [g,gbar,E,V] = leaky(V0, g, E, timesteps, dt)
V(1) = V0
g = g*ones(1,timesteps)
E = E*ones(1,timesteps)
gbar = g
for i = 1:timesteps-1
    dV(i) = -g(i)*(V(i)-E(i))*dt
    V(i+1)= V(i)+dV(i)
end
end