import bisect
import collections
import copy
import heapq
import itertools
import math
import sys
from collections import deque
from itertools import groupby, product

#template
#N = int(input())
#S = [input() for i in range(N)] #文字列list
#A,B = map(int,input().split())
#A = list(map(int,input().split()))

#Read List object
#A = []
#for i in range(N):
#    A.append(list(map(int,input().split())))

#文字列を1文字ずつlistに
#C = []
#for i in range(A):
#    S = input()
#    C.append(list(S))

#2つのsetの共通部分
#l1_l2_and = set(l1) & set(l2)
#setの共通しない部分
#l1_l2_and = set(l1) ^ set(l2)
#list,setの要素差分は普通に引き算

#make list
#B = [i for i in range(1,N+1)] 1 to N

#ソート
#for At, Bt in zip(A, B):
#    C.append((At,Bt))
#D = sorted(C) 1,2,3,4,5
#D = sorted(C, reverse=True) 5,4,3,2,1
#D = sorted(C, key=lambda x: (x[1])) Second value sort
#A.sort() [1,2,3,4,5]
#A.sort(reverse=True) [5,4,3,2,1]

#ゼロ埋め
#s = '1234'
#s_zero = s.zfill(8)
#print(s_zero)
# 00001234

#pop
#A = [1,2,3,4,5]
#A.pop(0) -> 1
#A.pop(-1) -> 5
#A = [2,3,4]
#del A[1]
#A = [2,4]

#list -> 文字列
#A = [1,2,3,4,5]
#B = "".join(A)
#print(B) -> 12345

#順列
#A=[1,2]
#for v in itertools.permutations(A, 2):
#    print(v)  #(1,2),(2,1)

#辞書の最大値
#max_v = max(d.values())
#print(max_v)

#辞書のソート
#dic2 = sorted(dic.items()) # keyでソート
#dic2 = sorted(dic.items(), key=lambda x:x[1]) #要素でソート

#辞書のループ
#d = {"test":3,"op",4}
#for k,v in d.items():

#各要素の出現回数の辞書を生成
#c = collections.Counter(list)

#要素が最大のkeyを取得
#print(max(c,key=c.get))

#誤差を考慮して比較
#math.isclose(0.1+0.1+0.1,0.3) -> True

#ASCII
#ord('A') #65
#chr(65)  #'A'

#配列のコピー
#A = [[0]*3 for i in range(5)] #3X5
#B.copy.deepcopy(A) #copy

#便利な出力
#judge = True
#print("Yes" if judge else "No")

#切り捨て math.floor(数値)
#切り上げ math.ceil(数値)

#大文字 str.upper()
#小文字 str.lower()

#最大公約数
#math.gcd(a,b)
#最小公倍数
#a*b//math.gcd(a,b)

#bisect
#リストはソート済みな!!!
#A = [1,3,5,7,9]
#N以上の数字で最もNに近いindexを返す(O(NlogN))
#bisect.bisect_left(A,8) -> 4
#bisect.bisect_left(A,0) -> 0
#bisect.bisect_left(A,5) -> 2
#bisect.bisect_left(A,100) -> 5
#A = [1,2,2,2,3]
#bisect.bisect_left(A,2) -> 1
#bisect.bisect_right(A,2) -> 4

#二分探索
#left = 0
#right = L
#while right - left > 1:
#    mid = (right+left)//2
#    if solve(mid):
#        left = mid
#    else:
#        right = mid

#bit全探索
#for pro in product((0, 1), repeat=5): #0,1の2**5通りのタプル
#    print(pro)
# -> (0,0,0,0,0) ~ (1,1,1,1,1)

#deque
#A = [1,2,3,4,5]
#O(1)
#A = deque(A)
#A.pop() A-> A[1,2,3,4]
#A.popleft() A-> [2,3,4]
#A.appendleft(0) A-> A[0,2,3,4]


#優先度付きQueの使い方 (いまいちわからん)
#最小値（最大値）を O(log⁡N)で取り出す
#要素を O(logN) で挿入する
#heapq.heapify(リスト)でリストを優先度付きキューに変換。
#heapq.heappop(優先度付きキュー (=リスト) )で優先度付きキューから最小値を取り出す。
#heapq.heappush(優先度付きキュー (=リスト) , 挿入したい要素)で優先度付きキューに要素を挿入(先頭)。

#尺取りテンプレート　(A13)
#right = 1
#cnt = 0
#for i in range(N):
#    while right < N and 条件:
#        right+=1
#    right-=1
#    print(i,right)
#    cnt+=right-i
