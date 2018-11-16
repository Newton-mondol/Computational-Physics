# Computational-Physics

* Physics
* Simulation

```Python
def minor(a, i, j):
    ar = []
    if len(a)-1!= 2:
        for i1 in range(len(a)):
            for j1 in range(len(a[0])):
                if i1 != i and j1 != j:
                    ar.append(a[i1][j1])
                    
    for i1 in range(len(a)):
        for j1 in range(len(a[0])):
            if i1 != i and j1 != j:
                ar.append(a[i1][j1])
    return ((-1) ** (i + j)) * (a[i][j]) * (ar[0] * ar[3] - ar[2] * ar[1])

```
