# รายการทดสอบ (test list)
# ขีดฆ่าออกเมื่อเทสต์ของรายการนั้นผ่านแล้ว
#
# [x] 200 g x 3 = 600 g
# [x] การคูณต้องไม่เปลี่ยนค่าของอ็อบเจ็กต์เดิม
# [x] ปริมาณสองค่าที่มีทั้งตัวเลขและหน่วยเท่ากันถือว่าเท่ากัน
# [x] 1 oz ไม่เท่ากับ 1 g
# [x] 200 g + 300 g = 500 g
# [x] 200 g + 1 oz แปลงผลลัพธ์เป็นกรัมโดยใช้อัตราแปลงหน่วย
# [ ] (200 g + 1 oz) x 2

from kitchen import Converter, Quantity


GRAMS_PER_OUNCE = 28


def grams(amount):
    return Quantity(amount, "g")


def ounces(amount):
    return Quantity(amount, "oz")


def converter_with_rates():
    converter = Converter()
    converter.add_rate("oz", "g", GRAMS_PER_OUNCE)
    return converter


def test_multiplication():
    flour = grams(200)
    assert flour.times(3) == grams(600)


def test_multiplication_by_two():
    flour = grams(200)
    assert flour.times(2) == grams(400)


def test_multiplication_returns_a_new_quantity():
    flour = grams(200)
    assert flour.times(3) == grams(600)
    assert flour.times(2) == grams(400)


def test_equality():
    assert grams(200) == grams(200)
    assert grams(200) != grams(300)


def test_grams_are_not_ounces():
    assert grams(1) != ounces(1)


def test_simple_addition():
    total = grams(200).plus(grams(300))
    converter = Converter()
    assert converter.reduce(total, "g") == grams(500)


def test_mixed_unit_addition():
    total = grams(200).plus(ounces(1))
    converter = converter_with_rates()
    assert converter.reduce(total, "g") == grams(200 + GRAMS_PER_OUNCE)


def test_scaling_a_mixed_unit_sum():
    doubled = grams(200).plus(ounces(1)).times(2)
    converter = converter_with_rates()
    assert converter.reduce(doubled, "g") == grams((200 + GRAMS_PER_OUNCE) * 2)
