from PIL import Image, ImageDraw
import math

def DrawFunction(img, equation_str: str, condition_str: str = "", scale=20, fg_color=(0, 0, 0)):

    width, height = img.size
    draw = ImageDraw.Draw(img)

    if '==' in equation_str:
        left, right = equation_str.split('==')
        expr = f"abs({left} - {right}) <= 0.05"
    else:
        expr = equation_str.replace('X', 'x').replace('Y', 'y').replace('^', '**')

    if condition_str:
        full_expr = f"({expr}) and ({condition_str})"
    else:
        full_expr = expr

    for px in range(width):
        for py in range(height):
            x = (px - width / 2) / scale
            y = -(py - height / 2) / scale

            try:
                result = eval(full_expr, {"x": x, "y": y, "__builtins__": {}}, {
                    "sqrt": math.sqrt,
                    "sin": math.sin,
                    "cos": math.cos,
                    "abs": abs,
                    "pi": math.pi,
                    "exp": math.exp,
                    "log": math.log
                })
            except:
                continue

            if result:
                draw.point((px, py), fill=fg_color)

def DrawAxes(img, scale=20, axis_color=(128, 128, 128), grid_color=(255, 255, 255), tick_step=1):

    width, height = img.size
    draw = ImageDraw.Draw(img)

    center_x = width // 2
    center_y = height // 2

    draw.line([(0, center_y), (width, center_y)], fill=axis_color)
    draw.line([(center_x, 0), (center_x, height)], fill=axis_color)

    # Сетка и подписи
    for x_val in range(-15, 16, tick_step):
        px = center_x + int(x_val * scale)
        if 0 <= px < width:
            draw.line([(px, 0), (px, height)], fill=grid_color)
            draw.text((px, center_y + 2), f"{x_val}", fill=axis_color)

    for y_val in range(-15, 16, tick_step):
        py = center_y - int(y_val * scale)
        if 0 <= py < height:
            draw.line([(0, py), (width, py)], fill=grid_color)
            draw.text((center_x + 2, py), f"{y_val}", fill=axis_color)

def CreateCanvas(width=400, height=400, bg_color=(222, 222, 222)):
    return Image.new("RGBA", (width, height), bg_color)

img = CreateCanvas(width=1000, height=1000)
DrawAxes(img, scale=33)
DrawFunction(img,"3*x+27==y","-10<=x and x<=-8",scale=33)
DrawFunction(img,"(-7/3)*x-47/3==y","-8<=x and x<=-5",scale=33)
DrawFunction(img,"(9-(x+5)**2)**(1/2)-7==y","-5<=x and x<=-2",scale=33)
DrawFunction(img,"-(49-(x+2)**2)**(1/2)==y","-2<=x and x<=5",scale=33)
DrawFunction(img,"x*2/3-10/3==y","5<=x and x<=8",scale=33)
DrawFunction(img,"4*x-30==y","8<=x and x<=9",scale=33)
img.show()

img2 = CreateCanvas()
DrawAxes(img2,scale=20)
DrawFunction(img2,"abs(x-4)+abs(y-4)<=3",fg_color=(180, 180, 180))
img2.show()

img3 = CreateCanvas()
DrawFunction(img3,"0==x","-7<=y and y<=10",scale=10,fg_color=(50, 200, 0))
DrawFunction(img3,"(x**2)/6-7==y","-10<=y and y<=9.5",scale=10,fg_color=(50, 200, 0))
DrawFunction(img3,"(x**48)*((1/4)**48)+(y+8)**48<=2**48",scale=10,fg_color=(100, 180, 50))
DrawFunction(img3,"(x/6)**16-18<=y","y<=-9",scale=10,fg_color=(100, 180, 50))

BParam=[-1,0,1]
AParam=[0,2.1,4.2]

for a in AParam:
    for b in BParam:
        DrawFunction(img3,f"(((x-9*{b})*cos({a})-(y-10-(-2*abs({b})))*sin({a}))**2)/12+((x-9*{b})*sin({a})+(y-10-(-2*abs({b})))*cos({a}))**2<=1",scale=10,fg_color=(250, 100, 100))
for b in BParam:
    DrawFunction(img3,f"(x-9*{b})**2+(y-8-2*abs(abs({b})-1))**2<=3",scale=10,fg_color=(200, 200, 0))
img3.show()
