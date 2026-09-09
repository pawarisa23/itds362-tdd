# รายการทดสอบ (test list)
# ขีดฆ่าออกเมื่อเทสต์ของรายการนั้นผ่านแล้ว
#
# [ ] 200 g x 3 = 600 g
# [ ] การคูณต้องไม่เปลี่ยนค่าของอ็อบเจ็กต์เดิม
# [ ] ปริมาณสองค่าที่มีทั้งตัวเลขและหน่วยเท่ากันถือว่าเท่ากัน
# [ ] 1 oz ไม่เท่ากับ 1 g
# [ ] 200 g + 300 g = 500 g
# [ ] 200 g + 1 oz แปลงผลลัพธ์เป็นกรัมโดยใช้อัตราแปลงหน่วย
# [ ] (200 g + 1 oz) x 2

from kitchen import Quantity


def test_multiplication():
    flour = Quantity(200)
    flour.times(3)
    assert flour.amount == 600


def test_multiplication_by_two():
    flour = Quantity(200)
    flour.times(2)
    assert flour.amount == 400
