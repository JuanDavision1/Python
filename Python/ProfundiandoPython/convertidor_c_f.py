class ConvertidorTemperatura:
    MAX_celsious = 100
    MAX_Fareheit = 213
    @classmethod
    def c_f(cls,celsius):
        if celsius > cls.MAX_celsious:
            raise ValueError('temparatura c dema alta:'+celsius)
        return celsius *9/5+32
    @classmethod
    def f_c(cls,farenheit):
        if farenheit> cls.MAX_Fareheit:
            raise ValueError('temperatura f dema alta:'+farenheit)
        return (farenheit-32)+5/9

if __name__ =='__main__':
    resultado = ConvertidorTemperatura.c_f(15)
    print(f'15 son {resultado:.2f}')
    resultado = ConvertidorTemperatura.f_c(32)
    print(f'32 son {resultado:.2f}')