# coding: utf-8
legend(['sin(2y)'])
clf()
plot(x,sin(x))
title('Sinusoids')
legend(['sin(2y)'])
plot(y,cos(y),'r')
clf()
plot(y,sin(y),'g',linewidth=2)
annotate('local max',xy=(1.5,1))
savefig('sin.png')
close()
