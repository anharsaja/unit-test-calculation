from unit_sistem import kalkulator
import unittest

class testOperasi(unittest.TestCase):
    def __init__(self, methodName: str = "Testing") -> None:
        super().__init__(methodName)
        self.operasi = kalkulator(20,5)

    def test_penjumlahan(self):
        hasil = self.operasi.penjumlahan()
        self.assertEqual(hasil, 20+5)
        
    def test_pengurangan(self):
        hasil = self.operasi.pengurangan()
        self.assertEqual(hasil, 20-5)

    def test_perkalian(self):
        hasil = self.operasi.perkalian()
        self.assertEqual(hasil, 20*5)

    def test_pembagian(self):
        hasil = self.operasi.pembagian()
        self.assertEqual(hasil, 20/5)

    def test_pembagian_by_zero(self):
    # Uji kasus ketika b adalah nol
        with self.assertRaises(ValueError):
            hasil = kalkulator(20,0)
            hasil.pembagian()


if __name__ == '__main__':
    unittest.main()