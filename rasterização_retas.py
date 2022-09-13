import matplotlib.pyplot as plt

def main():
    x1 = 3
    y1 = 2
    x2 = 9
    y2 = 4

    pontos = rasteriza_reta(x1, y1, x2, y2)
    xPoints = []
    yPoints = []
    
    for p in pontos:
        xPoints.append(p[0])
        yPoints.append(p[1])

    plotPoints(xPoints, yPoints)

def plotPoints(x, y):
    fig = plt.figure()    
    ax = fig.add_subplot(1,1,1)
    ax.yaxis.grid(color='gray', linestyle='dashed')
    ax.set_axisbelow(True)
    
    plt.plot(x, y, 'bo')
    plt.show()


def rasteriza_reta(x1, y1, x2, y2):
    def produz_fragmento():
        xm = int(x)
        ym = int(y)
        p = [xm, ym]
        return p

    lista = []
    dx = x2 - x1
    dy = y2 - y1
    m = dy/dx
    b = y2 - m * x2

    x = x1
    y = y1
    p = produz_fragmento()
    lista.append(p)

    while(x < x2):
        x += 1
        y = m * x + b
        p = produz_fragmento()
        lista.append(p)

    return lista

    
if __name__ == '__main__':
    main()
