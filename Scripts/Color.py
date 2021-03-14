from __future__ import division
from System.Drawing import Color as netColor

def HSVToColor(h, s, v):
    
    if s == 0.0: rgb = (v, v, v)
    i = int(h*6.) # XXX assume int() truncates!
    f = (h*6.)-i; p,q,t = int(255*(v*(1.-s))), int(255*(v*(1.-s*f))), int(255*(v*(1.-s*(1.-f)))); v*=255; i%=6
    if i == 0: rgb = (v, t, p)
    if i == 1: rgb = (q, v, p)
    if i == 2: rgb = (p, v, t)
    if i == 3: rgb = (p, q, v)
    if i == 4: rgb = (t, p, v)
    if i == 5: rgb = (v, p, q)
    return netColor.FromArgb(*rgb)

def RGBToHSV(r, g, b):
    maxc = max(r, g, b)
    minc = min(r, g, b)
    v = maxc
    if minc == maxc:
        return 0.0, 0.0, v / 255
    s = (maxc-minc) / maxc
    rc = (maxc-r) / (maxc-minc)
    gc = (maxc-g) / (maxc-minc)
    bc = (maxc-b) / (maxc-minc)
    if r == maxc:
        h = bc-gc
    elif g == maxc:
        h = 2.0+rc-bc
    else:
        h = 4.0+gc-rc
    h = (h/6.0) % 1.0
    return h, s, v / 255
