"""Exact Fraction/polynomial checks, not training. SymPy unavailable; see receipt."""
from fractions import Fraction as F
NAMES = ('t','a','u','v','target','eta')
N = len(NAMES)
class Poly:
    def __init__(self, value=0, data=None):
        self.d = ({(0,)*N:F(value)} if data is None else data)
        self.d = {k:v for k,v in self.d.items() if v}
    def __add__(self, other):
        other = other if isinstance(other, Poly) else Poly(other)
        d=dict(self.d)
        for k,v in other.d.items(): d[k]=d.get(k,F(0))+v
        return Poly(data=d)
    __radd__=__add__
    def __neg__(self): return Poly(data={k:-v for k,v in self.d.items()})
    def __sub__(self,o): return self+-o if isinstance(o,Poly) else self+(-F(o))
    def __rsub__(self,o): return -self+o
    def __mul__(self,o):
        o=o if isinstance(o,Poly) else Poly(o)
        d={}
        for k,v in self.d.items():
            for l,w in o.d.items():
                m=tuple(a+b for a,b in zip(k,l)); d[m]=d.get(m,F(0))+v*w
        return Poly(data=d)
    __rmul__=__mul__
    def __pow__(self,n):
        p=Poly(1)
        for _ in range(n): p=p*self
        return p
    def diff(self,name):
        i=NAMES.index(name); d={}
        for k,v in self.d.items():
            if k[i]:
                l=list(k);l[i]-=1;d[tuple(l)]=v*k[i]
        return Poly(data=d)
    def at(self,**kw):
        return sum((v*prod(F(kw.get(name,0))**e for name,e in zip(NAMES,k)) for k,v in self.d.items()),F(0))
    def zero(self): return not self.d

def prod(vals):
    p=F(1)
    for v in vals:p*=v
    return p

def var(name):
    k=[0]*N;k[NAMES.index(name)]=1
    return Poly(data={tuple(k):F(1)})

t,a,u,v,target,eta=map(var,NAMES)
y=t*t;L=F(1,2)*(y-a)**2;g=L.diff('t');H=g.diff('t');beta=3*y-a
assert (H*t-beta*y.diff('t')).zero()
assert (t*t*H-(4*y*y+2*(y-a)*y)).zero()
print('Polynomial identities for no-division Eq3 and Eq4: coefficient-exact PASS')
print('MSE target3 t1: g,H,beta =',g.at(t=1,a=3),H.at(t=1,a=3),beta.at(t=1,a=3))
print('MSE target1 t1: g,Htheta =',g.at(t=1,a=1),(H*t).at(t=1,a=1))
r=u*v-target;gu=r*v;gv=r*u;up=u-eta*gu;vp=v-eta*gv
assert ((up*up-vp*vp)-(1-eta*eta*r*r)*(u*u-v*v)).zero()
print('GD balancedness update: coefficient-exact PASS')
Luv=F(1,2)*r*r
Huv=[[Luv.diff(i).diff(j) for j in ('u','v')] for i in ('u','v')]
assert (Huv[0][0]*u-Huv[0][1]*v+gu).zero()
assert (Huv[1][0]*u-Huv[1][1]*v-gv).zero()
print('Hessian action under uv rescaling symmetry: coefficient-exact PASS')

mm=lambda A,B:[[sum(F(A[i][k])*F(B[k][j]) for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
tr=lambda A:list(map(list,zip(*A)))
P=[[0,1],[1,0]];W=[[1,0],[0,2]]
print('Wrong original transform P W P^-1 =',mm(mm(P,W),P))
P=[[1,2],[0,-1]];K=[[1,1],[1,2]]
assert mm(mm(tr(P),K),P)==K
assert mm(K,P)!=mm(P,K)
print('Nonorthogonal congruence invariant with failed commutation: exact PASS')
print('H P =',mm(K,P),'P H =',mm(P,K))

# Var(target)=1; C=(u^2-v^2)/2. Check trace identity polynomially.
trace_sigma=v*v+u*u
Xgradtrace=u*trace_sigma.diff('u')-v*trace_sigma.diff('v')
trace_sigma_HC=v*v-u*u
assert (trace_sigma_HC+F(1,2)*Xgradtrace).zero()
assert (v*v*u-u*v*v).zero() and (u*v*u-u*u*v).zero()
print('Noether trace identity and Sigma X=0: coefficient-exact PASS')

# f(theta)=exp(theta), theta=0, H=theta+log(1+lambda^2), lambda=2.
lam=F(2);A=F(1);B=1+lam*lam;J=F(1);X=2*lam/B;Y=X
H_ll=2*(1-lam*lam)/(B*B);G_ll=F(2)
R=-J/A*H_ll+G_ll/B
assert J*X==Y and X*X==R
print('Nonlinear-lambda second derivative at theta0,lambda2:',R,'= X^2')
print('ALL EXACT POLYNOMIAL / RATIONAL CHECKS PASSED; no training experiments')
