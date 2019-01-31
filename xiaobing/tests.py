from pyecharts import Bar  # 导入第三方库

# attr = ["{}day".format(i) for i in range(1, 8)]    #这样的话X坐标就是1day、2day、3day...
attr = ["Mon", "Feb", "Wed", "Thu", "Fri", "Sat", "Sun"]  # 这样X坐标就是星期
v1 = [1.49, 2.09, 4.03, 2.23, 5.26, 7.71, 7.56]
v2 = [0.3, 0.9, 0.2, 0.4, 0.7, 0.7, 0.6]
v3 = [18.15, 13.22, 11.28, 17.99, 18.7, 19.7, 15.6]

bar = Bar("XXX情况总览", "本图表展示过去一周的ABC情况")  # 这里是主标题和副标题
bar.add("A值", attr, v1, mark_line=["average"], mark_point=["max", "min"])  # 每一个值的名称以及要展现平均值和最大最小值
bar.add("B值", attr, v2, mark_line=["average"], mark_point=["max", "min"])
bar.add("C值", attr, v3, mark_line=["average"], mark_point=["max", "min"])
bar.render('statistics.html')  # 在/tmp文件夹里生成一个111.html文件
