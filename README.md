04-25-2018
+ 今天抽空补充,guess_solution.py能解决普通大小的k,性能是:
  + k = **100**,f = **1536**,耗时t= **0.2s**
  + k = **1000**,f = **51200000**,耗时t= **0.5s**
  + k = **22321**,f = **110536959860366672658432**,耗时t=**21.1s**
  + k = **100000**,f = **290142196707510978317649825651773931520**,耗时t=**133.8s**  
  + 以上计时都事先清空了__pycache__，我笔记本配置是 i5-2430M
  
+ 主要是发现count__(n)性能不错(O(log(N))的样子),如果有一个较好的上界估计,那再用二分查找,二分也是O(logN)
  + guess_solution.py用的上界是2<sup>k<sup>1/3</sup>-1</sup>3<sup>k<sup>1/3</sup>-1</sup>5<sup>k<sup>1/3</sup>-1</sup>。
  + 对于(n,m,n),如果(n',m',n')每一指数都小于,一共是(n+1)(m+1)(l+1),再考虑一项大于两项小于对于改进上述上界帮助不大。
  + 之前用2<sup>k</sup>作上界太粗糙，一个好的上界对于这种思路是关键。  

04-23-2018
+ 之前的数学解法不可行,考虑不周
+ 整数溢出的问题确实存在,涉及运算和存储是不同的,电脑可以算2<sup>1345</sup>的具体结果,但这个值不能再用于计算了
+ 删除了之前文件,新上传的测试过,可在初期小规模求解,本质是穷举
+ countFactors是O(logN), 性能很好,但不好利用
+ 测试的质数表 数据处理自 http://www.mathematical.com/primes0to1000k.html

04-22-2018
+ 数学方法应该是**O(1)**  （04-25-2018，思路有错）
+ countFactors可计算n以内满足2<sup>n</sup>3<sup>m</sup>5<sup>l</sup>的计数,p个因子应该是**O( (logN)<sup>p</sup>)**
+ 动态规划方法没弄出来,不确定怎样拆成子问题
+ 数学方法之前感觉(n, m, l) -->下一个(n', m', l') 是没规律的. "三维空间"的提示我没明白,取对数后是 aX+bY+cZ=d 的形式, d正比于原点到该平面距离的平方,但下一个距离应该不可递推吧
+ 关于穷举,应该不会整数溢出,当时我卡住了,因为我算过比45次幂更大的,但确实2<sup>45</sup> >> **4G**,我反应过来是整型存储其表示,2<sup>45</sup>需要45个bit,
而非2<sup>45</sup>个字节,上限应该是2<sup>**4G**+3</sup>
+ 我不是喜欢穷举,穷举思路比较直接,在比较小的范围可作为测试函数,大幂次的计算应该是O(logN)次乘法,且计算机擅长数值计算
+ 不优美的一种方法,不确定算不算穷举,（04-25-2018，思路有错）
S= n+ m+ l ,按照S的值将(n, m, l)的组合分类,同类的所有组合可以按照2 --> 3 --> 5 的优先级排序生成，也就是我面试说的“从高到低流向“，
这样可以合并有序序列，O(logN),也就是能排好所有 {(n, m, l) |(n, m, l) ∈ S<sub>i</sub> ,S<sub>i</sub> ≤S},
f(n,0,0)=2<sup>n</sup>能交错到的最下层是math.ceil ( log<sub>5</sub>2<sup>n</sup> ),
也就是类似取第K个素数去生成素数表的思路,但按照S<sub>i</sub> =x 从0-->infinity依次产生(n,m,l)时,S<sub>i</sub>和S<sub>j</sub>会交错,
算到S<sub>x</sub>时,可认为 n= math.ceil ( log<sub>5</sub>2<sup>S<sub>x</sub></sup> ),m=0,l=0,及之前的(m,n,l)已经排好了,不会有交错了
+ 在最新版的pychrm IDE 函数中import不会提示不规范
