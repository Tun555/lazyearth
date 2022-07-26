# LazyEmployee
## Employee OOP for Testing PyPI by Tun Kedsaro

[![N|Solid](https://cldup.com/dTxpPi9lDf.thumb.png)](https://nodesource.com/products/nsolid)
[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

PyPI: https://pypi.org/search/?q=lazyemployee
## Features

- Employee
- Engineer
- Programmer
- Sale
- set,get
- calculatesalary

โปรแกรมแชทนี้เป็นโปรแกรมที่เขียนขึ้นมาโดยใช้ Python โดยการเขียนแบบ OOP สำหรับใช้งานในการสร้าง class employee อย่างรวดเร็ว เพียงแค่มี Python อยู่ในคอมพิวเตอร์ก็สามารถใช้งานได้เลย เบื้องหลังการทำงานจะประกอบไปด้วย Engineer,Accounting,Sale



ปล. เวอร์ชั่นนี้ยังไม่สมบูรณ์ (เขียนแบบรีบๆ) เขียนเพื่อนำ concept OOP มาสร้าง library แล้วก็ upload ขึ้น Github กับ PyPI ต่อไป สำหรับนักพัฒนาสามารถนำ Source Code ไปพัฒนาต่อได้เต็มที่ ซึ่งก็คืออีกโปรเจคนึ่งนั้นแหละ เพราะว่า jupyter มันไม่สามารถ import def ได้เหมือนกับตัว คอมก็เลยใช้วิธีนี้เอา และก็ยังมีอีกหลาย library ที่เขียนดองเอาไว้ตั้งแต่สมัยเรียน ปี3, 4 แต่ว่ายังไม่ได้ upload  (เขียนไปงั้นแหละต้องใช้ความยาวระดับหนึ่งไม่งั้นไม่สามารถอัพได้)


## Plugins

Dillinger is currently extended with the following plugins.
Instructions on how to use them in your own application are linked below.

| Plugin | README |
| ------ | ------ |
| Employee | name,job,salary |
| Accounting | name,salary,age |
| Programmer | name,salary,exp,skill |
| Sale | name,salary,area |

## Tech

lazyemployee uses a number of open source projects to work properly:

- Python

## Installation

เปิด CMD / Terminal

```python
pip install lazyemployee
```

### วิธีใช้

[STEP 1]
- เปิด IDLE ขึ้นมาแล้วพิมพ์...

```python
from lazyemployee import Employee
from lazyemployee import Accounting,Programmer,Sale
```

- หรือเปิด cmd / terminal แล้วพิมพ์

```python
python -m lazyemployee
```

[STEP 2]
- ประกาศ class employee กรอก ชื่อ ตำแหน่งงาน และ เงินเดือน
- สามารถเรียกการแสดงผลได้โดยการใช้คำสั่ง detail()
- สามารถเปลี่ยนข้อมูลข้างในได้ด้วยการใช้ฟังก์ชัน setname() ,setsalary(),setjob()
- สามารถรับค่าข้อมูลข้างในได้ด้วยการใช้ฟังก์ชัน getname() ,getsalary(),getjob()


[STEP 3]
obj2= Accounting('Nan',20000,23)
obj2.detail()
print("\n")

obj3= Programmer('Xan',20000,3,'Python')
obj3.detail()
print("\n")

obj4= Sale('lin',20000,"A901")
obj4.detail()

## License

MIT
**Free Software, Hell Yeah!**

Develop by : Tun Kedsaro
FB: I dont tell you.
YouTube: Tun Kedsaro
