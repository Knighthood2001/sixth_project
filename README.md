# sixth_project
问卷星刷份数（面向过程）
首先要知道面向过程的问卷星刷份数是需要根据问卷不同而进行写代码，因此每份问卷都有其对应的代码，这也是面向过程版本的问卷星刷份数的最大缺点，费时间费人力敲代码，换来的只是代码清晰易懂。不过笔者最近在写面向对象版本的问卷星刷份数，这可以解决以上问题。
经过笔者尝试，问卷星刷份数一次只能刷50份，当刷到第51份时，则问卷星网站的点击验证会变成滑动验证，这时，笔者尝试过滑动验证，通过后问卷星份数并没有增加，因此可以得出当频繁的刷份数时，不管通不通过该滑动验证，份数都不会增加，这应该就是问卷星网站的防刷策略吧。问卷星（面向过程）4-有滑动验证码.py相对于问卷星（面向过程）3-增加了计数器.py只是增加了通过滑动验证功能，而这一功能在问卷星这里是行不通的，因此只需要使用问卷星（面向过程）3-增加了计数器.py即可。
需要注意的是，当刷完50份后，只需要过大半个小时或者一个小时后，即可再次运行该代码，问卷星份数就能继续增加。
