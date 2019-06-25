import cv2
import numpy as np


class sum():
    def __init__(self):
        self.out = []
        self.out1 = []
        self.inputs1 = input("第一个数组:")
        self.inputs2 = input("第二个数组:")
        self.in1 = ''
        self.in2 = ''
        self.in1_lis = []
        self.in2_lis = []
        self.symbol1 = False
        self.symbol2 = False

    def summation(self,in1_p,in2_p,out):
        n_sum = 0
        for i in range(len(in1_p) - 1, -1, -1):
            s = int(in1_p[i]) + int(in2_p[i]) + n_sum
            n_sum = 0
            if s >9:
                out.insert(0, str(s - 10))
                n_sum += 1
            else:
                out.insert(0, str(s))
            if i == 0 and n_sum == 1:
                out.insert(0,'1')
        if n_sum > 0:
            return True
        else:
            return False

    def differencing(self,in1_p,in2_p,out):
        n_differ = 0
        # print(in1_p,in2_p)
        for i in range(len(in1_p) - 1, -1, -1):
            s = int(in1_p[i])- n_differ - int(in2_p[i])
            n_differ = 0
            if s < 0:
                out.insert(0, str(10 + s))
                n_differ += 1
            else:
                out.insert(0, str(s))
            if i == 0 and n_differ == 1:
                out[0] = str(int(out[0])-1)
        if n_differ > 0:
            return True
        else:
            return False

    def list_differencing(self,in1_lis,in2_lis,out):
        out1 = []
        if len(in1_lis) > 1 and len(in2_lis) == 1 or len(in2_lis) > 1 and len(in1_lis) == 1:
            in1_p, in2_p = self.padding(in1_lis[0], in2_lis[0])
            self.differencing(in1_p,in2_p,out)
            if len(in1_lis)>1:
                out.append('.'+ in1_lis[1])
            else:
                out.append('.' + in2_lis[1])
        elif len(in1_lis) > 1 and len(in2_lis) > 1:
            new_out = []
            in1_p, in2_p = self.padding(in1_lis[0], in2_lis[0])
            in3_p, in4_p = self.paddingtd(in1_lis[1], in2_lis[1])
            state_dif = self.differencing(in3_p, in4_p, out1)
            self.differencing(in1_p,in2_p,out)
            if state_dif:
                in1_p, in2_p = self.padding(''.join(out), '1')
                self.differencing(in1_p,in2_p,new_out)
                new_out.append('.')
                out = new_out
            else:
                out.append('.')
            out = out + out1
        return out

    def list_summation(self,in1_lis,in2_lis,out):
        out1= []
        new_out = []
        if len(in1_lis)>1 and len(in2_lis) == 1 or len(in2_lis)>1 and len(in1_lis) == 1:
            in1_p,in2_p = self.padding(in1_lis[0],in2_lis[0])
            self.summation(in1_p,in2_p,out)
            if len(in1_lis)>1:
                out.append('.'+ in1_lis[1])
            else:
                out.append('.' + in2_lis[1])
        elif len(in1_lis) > 1 and len(in2_lis) > 1:
            in1_p, in2_p = self.padding(in1_lis[0], in2_lis[0])
            in3_p, in4_p = self.paddingtd(in1_lis[1], in2_lis[1])
            sum_state = self.summation(in3_p, in4_p, out1)
            self.summation(in1_p, in2_p, out)
            if sum_state:
                in1_p, in2_p = self.padding(''.join(out), '1')
                self.summation(in1_p, in2_p, new_out)
                new_out.append('.')
                out = new_out
                out1 = out1[1:]
                print(new_out,'---------------')
            else:
                out.append('.')
            # print(out,out1,'111111111111111111')
            out = out + out1
        else:
            in1_p, in2_p = self.padding(in1_lis[0], in2_lis[0])
            state_sum = self.summation(in1_p, in2_p, out)
            if state_sum:
                in1_p, in2_p = self.padding(''.join(out), '1')
                self.summation(in1_p, in2_p, new_out)
                out = new_out
        return out

    def padding(self,in1,in2):
        if len(in1)>len(in2):
            in2 = in2.zfill(len(in1))
            return in1, in2
        elif len(in2)>len(in1):
            in1 = in1.zfill(len(in2))
            return in1, in2
        else:
            return in1, in2

    def paddingtd(self,in1,in2):
        if len(in1)>len(in2):
            in2 = in2.ljust(len(in1),'0')
            return in1, in2
        elif len(in2)>len(in1):
            in1 = in1.ljust(len(in2),'0')
            return in1, in2
        else:
            return in1, in2


    def verify(self):
        in1 = self.inputs1
        in2 = self.inputs2
        if len(in1) == 0 or len(in2) == 0:
            print("请输入数字！！")
            return False
        # 获取为负的两个数组的状态
        if '-' == in1[0]:
            self.symbol1 = True
            in1 = self.in1 = in1[1:]
        if '-' == in2[0]:
            self.symbol2 = True
            in2 = self.in2 = in2[1:]

        self.in1_lis = in1.split('.')
        self.in2_lis = in2.split('.')

        if len(self.in1_lis) > 2 or len(self.in2_lis) > 2:
            print("请输入正确的数字！！")
            return False
        else:
            for i in self.in1_lis:
                if not i.isdigit():
                    print("第一个数组错误，请输入正确的数字！！")
                    return False
            for i in self.in2_lis:
                if not i.isdigit():
                    print("第二个数组错误，请输入正确的数字！！")
                    return False
        return True

    def Mains(self):
        # 验证数组
        ver = self.verify()
        if not ver:
            return


        in1_lis = self.in1_lis
        in2_lis = self.in2_lis
        symbol1 = self.symbol1
        symbol2 = self.symbol2

        if symbol1 and not symbol2 or symbol2 and not symbol1: #其中一个数组为负数
            le1 = len(in1_lis[0])
            le2 = len(in2_lis[0])
            if le1 > le2:
                out = self.list_differencing(in1_lis, in2_lis, self.out)
                if symbol1:
                    out.insert(0,'-')
                print(''.join(out))
            elif le2 > le1:
                out = self.list_differencing(in2_lis, in1_lis, self.out)
                if symbol2:
                    out.insert(0, '-')
                print(''.join(out))
            else:
                if int(in1_lis[0][0]) > int(in2_lis[0][0]):
                    out = self.list_differencing(in1_lis, in2_lis, self.out)
                else:
                    out = self.list_differencing(in2_lis, in1_lis, self.out)
                print(''.join(out))

        elif symbol1 and symbol2:# 都为负数
            out = self.list_summation(in1_lis, in2_lis, self.out)
            print('-'+''.join(out))
        else:#都为正数
            out = self.list_summation(in1_lis, in2_lis, self.out)
            print(''.join(out))

if __name__ == "__main__":

    while True:
        sum_test = sum()
        sum_test.Mains()
