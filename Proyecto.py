from os import system
system("cls")

class class_Valor:
    def __init__(self, atr_CrearArticulo, atr_CrearPrecio, atr_CrearMenu, atr_AccionMenuV,
                 atr_AccionMenuC, atr_CrearCategorias, atr_SelecionarCateg, atr_CrearCod,
                 atr_CrearCant, atr_BorrarUnd):
        self.atr_CrearArticulo = atr_CrearArticulo
        self.atr_CrearPrecio = atr_CrearPrecio
        self.atr_CrearMenu = atr_CrearMenu
        self.atr_AccionMenuV = atr_AccionMenuV
        self.atr_AccionMenuC = atr_AccionMenuC
        self.atr_CrearCategorias = atr_CrearCategorias
        self.atr_SelecionarCateg = atr_SelecionarCateg
        self.atr_CrearCod = atr_CrearCod
        self.atr_CrearCant = atr_CrearCant
        self.atr_BorrarUnd = atr_BorrarUnd
        

class class_Tienda(class_Valor):
    def __init__(self, atr_CrearArticulo, atr_CrearPrecio, atr_CrearMenu, atr_AccionMenuV,
                 atr_AccionMenuC, atr_CrearCategorias, atr_SelecionarCateg, atr_CrearCod,
                 atr_CrearCant, atr_BorrarUnd):
        
        super().__init__(atr_CrearArticulo, atr_CrearPrecio, atr_CrearMenu, atr_AccionMenuV,
                         atr_AccionMenuC, atr_CrearCategorias, atr_SelecionarCateg, atr_CrearCod,
                         atr_CrearCant, atr_BorrarUnd)
    
    array_CatgJugueteria = []
    array_UsersV = []
    array_PaswordsV = []
    array_UsersC = []
    array_PaswordsC = []
    array_ProdVendidos = []
    array_CatgHogar = []
    array_CatgRopa = []
    array_CatgFerreteria = []
    array_CatgLicoreria = []
    array_NombreC = []
    array_TelC = []
    array_DireC = []
    array_Cants = []

    
    def met_CrearArticulo(self):
        var_repeticion = 0
        while var_repeticion == 0:
            print("Por favor seleccione la categoria que le va a asignar a su producto:")
            print("1.- Jugueteria")
            print("2.- Hogar")
            print("3.- Ropa")
            print("4.- Ferreteria")
            print("5.- Licoreria")
            atr_CrearCategorias = int(input())
            if atr_CrearCategorias == 1:
                atr_CrearCod = int(input("Por favor digite el codigo del articulo: "))
                atr_CrearArticulo = input("Por favor digite el nombre del articulo: ")
                atr_CrearPrecio = float(input("Por favor digite el precio del articulo: "))
                atr_CrearCant = int(input("Por favor digite las cantidades del articulo: "))
                self.array_CatgJugueteria.append([[atr_CrearCod, atr_CrearArticulo], [atr_CrearPrecio, atr_CrearCant]])
                var_option = int(input("Felicidades articulo creado con exito \n por favor digite 1 si quiere crear otro articulo o cualquier otro número para volver al menú principal: "))
                print("Contenido de self.array_CatgJugueteria:", self.array_CatgJugueteria)
                if var_option == 1:
                    var_repeticion = 0
                else:
                    break
            if atr_CrearCategorias == 2:
                atr_CrearCod = int(input("Por favor digite el codigo del articulo: "))
                atr_CrearArticulo = input("Por favor digite el nombre del articulo: ")
                atr_CrearPrecio = float(input("Por favor digite el precio del articulo: "))
                atr_CrearCant = int(input("Por favor digite las cantidades del articulo: "))
                self.array_CatgHogar.append([[atr_CrearCod, atr_CrearArticulo], [atr_CrearPrecio, atr_CrearCant]])
                var_option = int(input("Felicidades articulo creado con exito \n por favor digite 1 si quiere crear otro articulo o cualquier otro número para volver al menú principal: "))
                if var_option == 1:
                    var_repeticion = 0
                else:
                    break
            if atr_CrearCategorias == 3:
                atr_CrearCod = int(input("Por favor digite el codigo del articulo: "))
                atr_CrearArticulo = input("Por favor digite el nombre del articulo: ")
                atr_CrearPrecio = float(input("Por favor digite el precio del articulo: "))
                atr_CrearCant = int(input("Por favor digite las cantidades del articulo: "))
                self.array_CatgRopa.append([[atr_CrearCod, atr_CrearArticulo], [atr_CrearPrecio, atr_CrearCant]])
                var_option = int(input("Felicidades articulo creado con exito \n por favor digite 1 si quiere crear otro articulo o cualquier otro número para volver al menú principal: "))
                if var_option == 1:
                    var_repeticion = 0
                else:
                    break
            if atr_CrearCategorias == 4:
                atr_CrearCod = int(input("Por favor digite el codigo del articulo: "))
                atr_CrearArticulo = input("Por favor digite el nombre del articulo: ")
                atr_CrearPrecio = float(input("Por favor digite el precio del articulo: "))
                atr_CrearCant = int(input("Por favor digite las cantidades del articulo: "))
                self.array_CatgFerreteria.append([[atr_CrearCod, atr_CrearArticulo], [atr_CrearPrecio, atr_CrearCant]])
                var_option = int(input("Felicidades articulo creado con exito \n por favor digite 1 si quiere crear otro articulo o cualquier otro número para volver al menú principal: "))
                if var_option == 1:
                    var_repeticion = 0
                else:
                    break
            if atr_CrearCategorias == 5:
                atr_CrearCod = int(input("Por favor digite el codigo del articulo: "))
                atr_CrearArticulo = input("Por favor digite el nombre del articulo: ")
                atr_CrearPrecio = float(input("Por favor digite el precio del articulo: "))
                atr_CrearCant = int(input("Por favor digite las cantidades del articulo: "))
                self.array_CatgLicoreria.append([[atr_CrearCod, atr_CrearArticulo], [atr_CrearPrecio, atr_CrearCant]])
                var_option = int(input("Felicidades articulo creado con exito \n por favor digite 1 si quiere crear otro articulo o cualquier otro número para volver al menú principal: "))
                if var_option == 1:
                    var_repeticion = 0
                else:
                    break

    def met_AccionesVendedor(self):
        var_RepI = 0

        while var_RepI == 0:
            var_inve = 0
            var_Int = 0
            var_valcli = 0
            var_Pv = 0
            var_Vent = 0
            var_Revent = 0

            print("Bienvenido a su cuenta, por favor seleccione lo que desea hacer:")
            print("1.-Crear un artículo")
            print("2.-Revisar Historial de ventas")
            print("3.-Consultar mi inventario")
            print("4.-Revisar mis clientes")
            print("5.-Volver al menú anterior")
            atr_AccionMenuV = int(input())

            obj_03 = class_Validacion(0, 0, 0, atr_AccionMenuV, 0, 0, 0, 0,0)

            if obj_03.met_ValidarAccMenu() == True:
                if atr_AccionMenuV == 1:
                    self.met_CrearArticulo()
                if atr_AccionMenuV == 2:
                    print("Lista de productos vendidos\n")
                    if len(self.array_ProdVendidos) == 0:
                        while var_Pv == 0:
                            print("No se han vendido productos todavía.")
                            var_Pv = int(input("Presione 1 si quiere volver al menú principal: "))
                            if var_Pv == 1:
                                break
                            else:
                                print("Digitó una opción incorrecta, por favor inténtelo de nuevo.")
                                var_Pv = 0
                    else:
                        for i in range(len(self.array_ProdVendidos)):
                            print("Se compraron:", self.array_Cants[i], "unidades del producto:", self.array_ProdVendidos[i], "y ha sido comprado por:", self.array_NombreC[i], "| Teléfono:", self.array_TelC[i], "| Dirección:", self.array_DireC[i])
                        while var_Revent == 0:
                            var_Vent = int(input("\nEstos son todos los productos que ha vendido, por favor digite 1 si quiere volver al menú anterior: "))
                            if var_Vent == 1:
                                break
                            else:
                                print("Digitó una opción incorrecta, por favor vuelva a intentarlo.\n")
                                var_Revent = 0
                if atr_AccionMenuV == 3:
                    print("Lista de productos de su inventario")
                    print("\nProductos Jugueteria")
                    for item in self.array_CatgJugueteria:
                        print("Nombre:", item[0][1], "| Unidades:", item[1][1])
                    if len(self.array_CatgJugueteria) == 0:
                        print("No hay articulos en esta categoria")

                    print("\nProductos Hogar")
                    for self.array_CatgHogar in self.array_CatgHogar:
                        print("Nombre:", self.array_CatgHogar[0][1], "| Unidades:", self.array_CatgHogar[1][1])
                    if len(self.array_CatgHogar) == 0:
                        print("No hay articulos en esta categoria")

                    print("\nProductos Ropa")
                    for self.array_CatgRopa in self.array_CatgRopa:
                        print("Nombre:", self.array_CatgRopa[0][1], "| Unidades:", self.array_CatgRopa[1][1])
                    if len(self.array_CatgRopa) == 0:
                        print("No hay articulos en esta categoria")

                    print("\nProductos Ferreteria")
                    for self.array_CatgFerreteria in self.array_CatgFerreteria:
                        print("Nombre:", self.array_CatgFerreteria[0][1], "| Unidades:", self.array_CatgFerreteria[1][1])
                    if len(self.array_CatgFerreteria) == 0:
                        print("No hay articulos en esta categoria")

                    print("\nProductos Licoreria")
                    for self.array_CatgLicoreria in self.array_CatgLicoreria:
                        print("Nombre:", self.array_CatgLicoreria[0][1], "| Unidades:", self.array_CatgLicoreria[1][1])
                    if len(self.array_CatgLicoreria) == 0:
                        print("No hay articulos en esta categoria")

                    while var_Int == 0:
                        var_inve = int(input("\nEste es todo su inventario, por favor digite 1 si quiere volver al menú anterior: "))
                        if var_inve == 1:
                            break
                        else:
                            print("Digitó una opción incorrecta, por favor vuelva a intentarlo")
                            var_Int = 0
                if atr_AccionMenuV == 4:
                    print("Sus clientes son:")
                    for i in range(len(self.array_NombreC)):
                        print("\n -", self.array_NombreC[i])
                    if len(self.array_NombreC) == 0:
                        while var_valcli == 0:
                            var_valcli = int(input("\nNo hay clientes todavia \n \nDigite 1 si quiere volver al menu anterior: "))
                            if var_valcli == 1:
                                break
                            else:
                                print("Digitó una opción incorrecta, por favor vuelva a intentarlo")
                                var_valcli = 0
                    while var_valcli == 0:
                        var_valcli = int(input("\nEstos son todos sus clientes, digite 1 si quiere volver al menú anterior: "))
                        if var_valcli == 1:
                            break
                        else:
                            print("Digitó una opción incorrecta, por favor vuelva a intentarlo")
                            var_valcli = 0
                if atr_AccionMenuV == 5:
                    break

                if obj_03.met_ValidarAccMenu() == False:
                    print("Digitó una opción diferente, por favor intentelo de nuevo")
                    var_RepI = 0
        

    def met_AccionesComprador(self):
        var_repe = 0

        while var_repe == 0:
            var_rep = 0
            var_Comprar = 0
            var_elec = ""
            var_sw = False
            var_NomC = ""
            var_TelC = ""
            var_DireC = ""

            print("Bienvenido a su cuenta, por favor seleccione lo que desea hacer:")
            print("1.- Comprar un artículo")
            print("2.- Volver al menú anterior")
            atr_AccionMenuC = int(input())
            if atr_AccionMenuC == 1:
                while var_rep == 0:
                    print("Por favor seleccione la categoría del producto que desea comprar:")
                    print("1.- Juguetería")
                    print("2.- Hogar")
                    print("3.- Ropa")
                    print("4.- Ferretería")
                    print("5.- Licorería")
                    atr_SelecionarCateg = int(input())
                    if atr_SelecionarCateg == 1:
                        if len(self.array_CatgJugueteria) == 0:
                            print("No hay artículos en esta categoría")
                            break
                        print("Lista de productos:")
                        for producto in self.array_CatgJugueteria:
                            print(" Nombre:", producto[0][1], " Precio: $", producto[1][0], " Cantidades:", producto[1][1])
                        print("Digite 1 si quiere comprar algún artículo o cualquier otro número para volver al menú principal")
                        var_Comprar = int(input())
                        if var_Comprar == 1:
                            print("Digite el nombre del artículo que quiere comprar: ", end="")
                            var_elec = input()
                            for producto in self.array_CatgJugueteria:
                                if producto[0][1] == var_elec:
                                    self.array_ProdVendidos.append(var_elec)
                                    print("Digite cuántas cantidades quiere comprar: ", end="")
                                    atr_BorrarUnd = int(input())
                                    self.array_Cants.append(atr_BorrarUnd)
                                    if atr_BorrarUnd > producto[1][1]:
                                        print("Cantidad no permitida, por favor inténtelo de nuevo\n")
                                        var_sw = True
                                        break
                                    if atr_BorrarUnd <= producto[1][1]:
                                        producto[1][1] =  producto[1][1] - atr_BorrarUnd
                                        if producto[1][1] == 0:
                                            del self.array_CatgJugueteria[self.array_CatgJugueteria.index(producto)]
                                    print("\nDigite los siguientes datos:")
                                    print("Nombre: ", end="")
                                    var_NomC = input()
                                    self.array_NombreC.append(var_NomC)
                                    print("Telefono: ", end="")
                                    var_TelC = input()
                                    self.array_TelC.append(var_TelC)
                                    print("Dirección: ", end="")
                                    var_DireC = input()
                                    self.array_DireC.append(var_DireC)
                                    print("\nFelicitaciones. Artículo comprado con éxito.")
                                    var_sw = True
                                    break
                            if var_sw == False:
                                print("El nombre que digitaste es incorrecto, por favor vuelva a intentarlo.\n")
                                var_repe = 0
                            break
                        else:
                            var_repe = 0
                            break
                    if atr_SelecionarCateg == 2:
                        if len(self.array_CatgHogar) == 0:
                            print("No hay artículos en esta categoría.\n")
                            break
                        print("Lista de productos:\n")
                        for producto in self.array_CatgHogar:
                            print(" Nombre:", producto[0][1], " Precio: $", producto[1][0], " Cantidades:", producto[1][1])
                        print("Digite 1 si quiere comprar algún artículo o cualquier otro número para volver al menú principal: ", end="")
                        var_Comprar = int(input())
                        if var_Comprar == 1:
                            print("Digite el nombre del artículo que quiere comprar: ", end="")
                            var_elec = input()
                            for producto in self.array_CatgHogar:
                                if producto[0][1] == var_elec:
                                    self.array_ProdVendidos.append(var_elec)
                                    print("Digite cuántas cantidades quiere comprar: ", end="")
                                    atr_BorrarUnd = int(input())
                                    self.array_Cants.append(atr_BorrarUnd)
                                    if atr_BorrarUnd > producto[1][1]:
                                        print("Cantidad no permitida, por favor inténtelo de nuevo.\n")
                                        var_sw = True
                                        break
                                    if atr_BorrarUnd <= producto[1][1]:
                                            producto[1][1] =  producto[1][1] - atr_BorrarUnd
                                            if producto[1][1] == 0:
                                                del self.array_CatgHogar[self.array_CatgHogar.index(producto)]
                                    print("\nDigite los siguientes datos:")
                                    print("Nombre: ", end="")
                                    var_NomC = input()
                                    self.array_NombreC.append(var_NomC)
                                    print("Telefono: ", end="")
                                    var_TelC = input()
                                    self.array_TelC.append(var_TelC)
                                    print("Dirección: ", end="")
                                    var_DireC = input()
                                    self.array_DireC.append(var_DireC)
                                    print("\nFelicitaciones. Artículo comprado con éxito.")
                                    var_sw = True
                                    break
                            if var_sw == False:
                                print("El nombre que digitaste es incorrecto, por favor vuelva a intentarlo.\n")
                                var_repe = 0
                            break
                        else:
                            var_repe = 0
                            break
                    if atr_SelecionarCateg == 3:
                        if len(self.array_CatgRopa) == 0:
                            print("No hay artículos en esta categoría.\n")
                            break
                        print("Lista de productos:\n")
                        for producto in self.array_CatgRopa:
                            print(" Nombre:", producto[0][1], " Precio: $", producto[1][0], " Cantidades:", producto[1][1])
                        print("Digite 1 si quiere comprar algún artículo o cualquier otro número para volver al menú principal: ", end="")
                        var_Comprar = int(input())
                        if var_Comprar == 1:
                            print("Digite el nombre del artículo que quiere comprar: ", end="")
                            var_elec = input()
                            for producto in self.array_CatgRopa:
                                if producto[0][1] == var_elec:
                                    self.array_ProdVendidos.append(var_elec)
                                    print("Digite cuántas cantidades quiere comprar: ", end="")
                                    atr_BorrarUnd = int(input())
                                    self.array_Cants.append(atr_BorrarUnd)
                                    if atr_BorrarUnd > producto[1][1]:
                                        print("Cantidad no permitida, por favor inténtelo de nuevo.\n")
                                        var_sw = True
                                        break
                                    if atr_BorrarUnd <= producto[1][1]:
                                            producto[1][1] =  producto[1][1] - atr_BorrarUnd
                                            if producto[1][1] == 0:
                                                del self.array_CatgRopa[self.array_CatgRopa.index(producto)]
                                    print("\nDigite los siguientes datos:")
                                    print("Nombre: ", end="")
                                    var_NomC = input()
                                    self.array_NombreC.append(var_NomC)
                                    print("Telefono: ", end="")
                                    var_TelC = input()
                                    self.array_TelC.append(var_TelC)
                                    print("Dirección: ", end="")
                                    var_DireC = input()
                                    self.array_DireC.append(var_DireC)
                                    print("\nFelicitaciones. Artículo comprado con éxito.")
                                    var_sw = True
                                    break
                            if var_sw == False:
                                print("El nombre que digitaste es incorrecto, por favor vuelva a intentarlo.\n")
                                var_repe = 0
                            break
                        else:
                            var_repe = 0
                            break
                    if atr_SelecionarCateg == 4:
                        if len(self.array_CatgFerreteria) == 0:
                            print("No hay articulos en esta categoria")
                            break
                        print("Lista de productos:")
                        for producto in self.array_CatgFerreteria:
                            print(" Nombre:", producto[0][1], " Precio: $", producto[1][0], " Cantidades:", producto[1][1])
                        var_Comprar = input("Digite 1 si quiere comprar algún articulo o cualquier otro número para volver al menú principal\n")
                        if var_Comprar == "1":
                            var_elec = input("Digite el nombre del articulo que quiere comprar: ")
                            for producto in self.array_CatgFerreteria:
                                if producto[0][1] == var_elec:
                                    self.array_ProdVendidos.append(var_elec)
                                    atr_BorrarUnd = int(input("Digite cuantas cantidades quiere comprar: "))
                                    self.array_Cants.append(atr_BorrarUnd)
                                    if atr_BorrarUnd > producto[1][1]:
                                        print("Cantidad no permitida, por favor intentelo de nuevo")
                                        var_sw = True
                                        break
                                    if atr_BorrarUnd <= producto[1][1]:
                                            producto[1][1] =  producto[1][1] - atr_BorrarUnd
                                            if producto[1][1] == 0:
                                                del self.array_CatgFerreteria[self.array_CatgFerreteria.index(producto)]
                                    
                                    print("\nDigite los siguientes datos:")
                                    var_NomC = input("Nombre: ")
                                    self.array_NombreC.append(var_NomC)
                                    var_TelC = input("Telefono: ")
                                    self.array_TelC.append(var_TelC)
                                    var_DireC = input("Dirección: ")
                                    self.array_DireC.append(var_DireC)
                                    print("\nFelicitaciones Articulo comprado con exito")
                                    var_sw = True
                                    break
                            if var_sw == False:
                                print("El nombre que digitaste es incorrecto, por favor vuelva a intentarlo")
                                var_repe = 0
                                break
                            break
                        else:
                            var_repe = 0
                            break
                    if atr_SelecionarCateg == 5:
                        if len(self.array_CatgLicoreria) == 0:
                            print("No hay articulos en esta categoria")
                            break
                        print("Lista de productos:")
                        for producto in self.array_CatgLicoreria:
                            print(" Nombre:", producto[0][1], " Precio: $", producto[1][0], " Cantidades:", producto[1][1])
                        var_Comprar = input("Digite 1 si quiere comprar algún articulo o cualquier otro número para volver al menú principal\n")
                        if var_Comprar == "1":
                            var_elec = input("Digite el nombre del articulo que quiere comprar: ")
                            for producto in self.array_CatgLicoreria:
                                if producto[0][1] == var_elec:
                                    self.array_ProdVendidos.append(var_elec)
                                    atr_BorrarUnd = int(input("Digite cuantas cantidades quiere comprar: "))
                                    self.array_Cants.append(atr_BorrarUnd)
                                    if atr_BorrarUnd > producto[1][1]:
                                        print("Cantidad no permitida, por favor intentelo de nuevo")
                                        var_sw = True
                                        break
                                    if atr_BorrarUnd <= producto[1][1]:
                                            producto[1][1] =  producto[1][1] - atr_BorrarUnd
                                            if producto[1][1] == 0:
                                                del self.array_CatgLicoreria[self.array_CatgLicoreria.index(producto)]
                                    
                                    print("\nDigite los siguientes datos:")
                                    var_NomC = input("Nombre: ")
                                    self.array_NombreC.append(var_NomC)
                                    var_TelC = input("Telefono: ")
                                    self.array_TelC.append(var_TelC)
                                    var_DireC = input("Dirección: ")
                                    self.array_DireC.append(var_DireC)
                                    print("\nFelicitaciones Articulo comprado con exito")
                                    var_sw = True
                                    break
                            if var_sw == False:
                                print("El nombre que digitaste es incorrecto, por favor vuelva a intentarlo")
                                var_repe = 0
                                break
                            break
                        else:
                            var_repe = 0
                            break
            elif atr_AccionMenuC == 2:
                    break
            if atr_AccionMenuC != 1 and atr_AccionMenuC != 2:
                print("Seleccionó una opción erronea, por favor intentelo de nuevo")
                var_repe = 0

    def met_CrearMenu(self):
        var_Rep = 0
        while var_Rep == 0:
            print("Bienvenido. Por favor, seleccione la opción con la que desea ingresar:")
            print("1.- Ingresar como vendedor")
            print("2.- Ingresar como comprador")
            print("3.- Para salir")
            atr_CrearMenu = int(input())

            obj_01 = class_Validacion(0, 0, atr_CrearMenu, 0, 0, 0, 0, 0,0)
            if obj_01.met_ValidarMenu() == True:
                if atr_CrearMenu == 1:
                    obj_02 = class_Usuario("0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                    obj_02.met_CrearVendedor()
                if atr_CrearMenu == 2:
                    obj_02 = class_Usuario("0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                    obj_02.met_CrearComprador()
                if atr_CrearMenu == 3:
                    print("Gracias por usar el programa.")
                    break
            if obj_01.met_ValidarMenu() == False:
                print("Digitó una opción incorrecta, por favor inténtelo de nuevo")
                var_Rep = 0
                
    


class class_Usuario(class_Valor):
    def __init__(self, atr_CrearArticulo, atr_CrearPrecio, atr_CrearMenu, atr_AccionMenuV,
                 atr_AccionMenuC, atr_CrearCategorias, atr_SelecionarCateg, atr_CrearCod,
                 atr_CrearCant, atr_BorrarUnd, atr_CrearUserC, atr_CrearUserV):
        
        super().__init__(atr_CrearArticulo, atr_CrearPrecio, atr_CrearMenu, atr_AccionMenuV,
                         atr_AccionMenuC, atr_CrearCategorias, atr_SelecionarCateg, atr_CrearCod,
                         atr_CrearCant, atr_BorrarUnd)

    array_CatgJugueteria = []
    array_UsersV = []
    array_PaswordsV = []
    array_UsersC = []
    array_PaswordsC = []
    array_ProdVendidos = []
    array_CatgHogar = []
    array_CatgRopa = []
    array_CatgFerreteria = []
    array_CatgLicoreria = []
    array_NombreC = []
    array_TelC = []
    array_DireC = []
    array_Cants = []

    
    def met_CrearVendedor(self):
        var_rep = 0

        while var_rep == 0:
            var_rep1 = 0
            var_UsuarioV = ""
            var_PaswordV = 0
            var_ValidUserV = ""
            var_sw1 = False
            var_ValidPwV = 0
            var_sw2 = False
            var_termUser = 0

            
            atr_CrearUserV = int(input("Bienvenido al apartado de vendedores, por favor seleccione una opción:\n"
            "1.- Para crear una cuenta\n"
            "2.- Para iniciar sesión\n"
            "3.- Para volver al menú principal\n"))

            obj_02 = class_Validacion(0, 0, 0, 0, 0, 0, atr_CrearUserV, 0,0)
            if obj_02.met_ValidarUserV() == True: 
                if atr_CrearUserV == 1:
                    print("Por favor ingrese el nombre de usuario que desea crear:")
                    var_UsuarioV = input()
                    self.array_UsersV.append(var_UsuarioV)
                    print("Por favor ingrese la contraseña que desea crear:")
                    var_PaswordV = int(input())
                    self.array_PaswordsV.append(var_PaswordV)
                    print("Felicitaciones, cuenta creada exitosamente.")
                    print("Digite 1 si quiere iniciar sesión o cualquier otro número para volver al menú principal:")
                    var_termUser = int(input())
                    if var_termUser == 1:
                        atr_CrearUserV = 2
                    else:
                        var_rep = 0

                if atr_CrearUserV == 2:
                    while var_rep1 == 0:
                        print("Por favor ingrese su nombre de usuario:")
                        var_ValidUserV = input()
                        for i in range(len(self.array_UsersV)):
                            if self.array_UsersV[i] == var_ValidUserV:
                                var_sw1 = True
                        if var_sw1 == True:
                            print("Por favor ingrese su contraseña:")
                            var_ValidPwV = int(input())
                            for j in range(len(self.array_PaswordsV)):
                                if self.array_PaswordsV[j] == var_ValidPwV:
                                    var_sw2 = True
                            if var_sw2 == True:
                                obj_10 = class_Tienda("0", 0, 0, 0, 0, 0, 0, 0, 0, 0)
                                obj_10.met_AccionesVendedor()
                                var_rep1 = 1
                            else:
                                print("La contraseña que ingresó es incorrecta, por favor repita el proceso.")
                                var_rep1 = 0
                        else:
                            print("El nombre de usuario que ingresó es incorrecto.")
                            print("Digite 1 si quiere volver a intentarlo o cualquier otro número para volver al menú principal:")
                            var_rep1 = int(input())
                            if var_rep1 == 1:
                                var_rep1 = 0
                            else:
                                var_rep1 = 1

                if atr_CrearUserV == 3:
                    break
            if obj_02.met_ValidarUserV() == False:
                    print("Digitó una opción incorrecta, por favor inténtelo de nuevo.")
                    var_rep = 0

    def met_CrearComprador(self):
        var_repC = 0
        
        while var_repC == 0:
            """ var_UsuarioC = ""
            var_PaswordC = 0 """
            var_ValidUserC = ""
            var_rep1C = 0
            var_sw1C = False
            var_ValidPwC = 0
            var_sw2C = False
            var_Guser = 0
            var_repetir = 0
            
            print("Bienvenido al apartado de compradores, por favor seleccione una opción:")
            print("1.-Para crear una cuenta")
            print("2.-Para iniciar sesión")
            print("3.-Para volver al menú principal")
            atr_CrearUserC = int(input("Seleccione una opción: "))
            
            obj_09 = class_Validacion(0, 0, 0, 0, 0, atr_CrearUserC,0, 0,0)
            
            if obj_09.met_ValidarUserC() == True:
                if atr_CrearUserC == 1:
                    self.array_UsersC.append([input("por favor ingrese un nombre de usuario: ")])
                    self.array_PaswordsC.append([input("por favor ingrese una contraseña: ")])
                    print("Felicitaciones, cuenta creada exitosamente. \nDigite 1 si quiere iniciar sesión o cualquier otro número para volver al menú principal: ")
                    var_Guser = int(input())
                    var_repC = 0
                    
                    if var_Guser == 1:
                        atr_CrearUserC = 2
                    else:
                        var_repC = 0
                
                if atr_CrearUserC == 2:
                    while var_rep1C == 0:
                        print("Por favor ingrese su nombre de usuario:")
                        var_ValidUserC = input()
                        
                        for i in range(len(self.array_UsersC)):
                            if self.array_UsersC[i] == self.array_UsersC[i]:
                                var_sw1C = True
                        
                        if var_sw1C == True:
                            print("Por favor ingrese su contraseña:")
                            var_ValidPwC = int(input())
                            
                            for j in range(len(self.array_PaswordsC)):
                                if self.array_PaswordsC[j] == self.array_PaswordsC[j]:
                                    var_sw2C = True
                            
                            if var_sw2C == True:
                                obj_11 = class_Tienda("0", 0, 0, 0, 0, 0, 0, 0, 0, 0)
                                obj_11.met_AccionesComprador()
                                var_rep1C = 1
                            else:
                                print("La contraseña que ingresó es incorrecta, por favor repita el proceso")
                                var_rep1C = 0
                        else:
                            print("El nombre de usuario que ingresó es incorrecto. Digite 1 si quiere intentarlo de nuevo o cualquier otro número para volver al menú principal:")
                            var_repetir = int(input())
                            
                            if var_repetir == 1:
                                var_rep1C = 0
                            else:
                                var_rep1C = 1
                                
                if atr_CrearUserC == 3:
                    break
            if obj_09.met_ValidarUserC() == False:
                print("Digitó una opción incorrecta, por favor intentelo de nuevo")
                var_repC = 0



class class_Validacion:
    def __init__(self, atr_CrearArticulo, atr_CrearPrecio, atr_CrearMenu, atr_AccionMenuV, atr_SelecionarCateg,atr_CrearUserC,
                 atr_CrearUserV,atr_AccionMenuC,atr_CrearCategorias):
        
        self.atr_CrearArticulo = atr_CrearArticulo
        self.atr_CrearPrecio = atr_CrearPrecio
        self.atr_CrearMenu = atr_CrearMenu
        self.atr_AccionMenuV = atr_AccionMenuV
        self.atr_SelecionarCateg = atr_SelecionarCateg
        self.atr_CrearUserC = atr_CrearUserC
        self.atr_CrearUserV = atr_CrearUserV
        self.atr_AccionMenuC = atr_AccionMenuC
        self.atr_CrearCategorias = atr_CrearCategorias
        

    def met_ValidarMenu(self):
        if self.atr_CrearMenu >= 1 and self.atr_CrearMenu <= 3:
            return True
        else:
            return False

    def met_ValidarUserC(self):
        if self.atr_CrearUserC >= 1 and self.atr_CrearUserC <= 3:
            return True
        else:
            return False

    def met_ValidarAccMenu(self):
        if self.atr_AccionMenuV >= 1 and self.atr_AccionMenuV <= 5:
            return True
        else:
            return False

    def met_ValidarUserV(self):
        if self.atr_CrearUserV >= 1 and self.atr_CrearUserV <= 3:
            return True
        else:
            return False

    def met_ValidarCateg(self):
        if self.atr_SelecionarCateg >= 1 and self.atr_SelecionarCateg <= 5:
            return True
        else:
            return False

    def met_ValidarAccMenuC(self):
        if self.atr_AccionMenuC >= 1 and self.atr_AccionMenuC <= 2:
            return True
        else:
            return False

obj_07 = class_Tienda("0", 0, 0, 0, 0, 0,0,0,0,0)
obj_07.met_CrearMenu()


