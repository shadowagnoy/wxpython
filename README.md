# python wxpython 学习
- 简介
    - wxPython（最成熟的跨平台python GUI工具包）
- 使用手册：https://www.wxpython.org/Phoenix/docs/html/
- WxPython的程序结构
    -
- 代码介绍
    - gui1.py 
- 补充说明
    - id:
        - 说明:wxpython对每个控件都会分配一个唯一的整数型ID，方便调用，类十余c中的Handle。ID在时间响应中必不可少。创建控件时如果ID为-1时，会自动分配一个ID。这样就不能对ID进行引用。其实可以使用控件对象的GetId方法进行获取.
        - 生成方式:
            - 方法1:前置每个控件的ID（自己设置的名称）,使用列表生成器生成 [Btn_1_ID,Btn_2_ID,Btn_3_ID] = [wx.NewId() for _init_cj in range(3)]有几个控件就设置循环几次然后在生成控件时进行调用
            - 方法2:使用类的属性来预先分配，然后控件类对他进行继承，每个控件类句读一个属于他的id属性
      
        
