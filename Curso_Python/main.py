#import operaciones as op
import package.suma
import sys 
import pprint as p


def main():
    # res = op.suma(2,2)
    # resResta = op.resta(5,2)
    # print('el resultado de la operacion es', res)
    # print('el resultado de la operacion es', resResta)
    #print(op.comoMeLLamo())
    # op = o.Operador()
    # print(op.multiplicador(8,7))
    #print(op.PI)
    #p.pprint(sys.path)
    
    #nombre del paquete luego el modulo lugo la funcion
    #funcion
    print(package.suma.suma(1,3))
    
    #clase instanciamos el objeto
    np = package.suma.Multiplicador()
    #se utiliza el metodo de la clase
    print(np.multiplica(5,3))

    
    
    
    
if __name__ == '__main__':
    main()