
class C_menu:
    def __init__(self,P_type,p_href,p_desc):
        self.type=P_type
        self.href=p_href
        self.desc=p_desc
    def getdesc(self):
        return self.desc
    def gethref(self):
        return self.href
    def gettype(self):
        tp=self.type
        # print(tp)
        return  tp
    def istypeli(self):
        if self.type=="li":
            return True
        return False
    def istypeulopen(self):
        
        if self.type=="<ul>":
            return True
        return False
    def istypeliclose(self):
        if self.type=="</li>":
            return True
        return False

    def istypeulclose(self):
        if self.type=="</ul>":
            return True
        return False

def createmenu(auth=True):
    menuret=[]
    menuret.append(C_menu("li","/","home"))
    if auth==True:
        menuret.append(C_menu("li","/bom/","Mis Expensas"))
        menuret.append(C_menu("<ul>","",""))
        menuret.append(C_menu("li","/bom/","Estado de Cuenta"))
        menuret.append(C_menu("li","/bom/upd","Informar Pago"))
        menuret.append(C_menu("</ul>","",""))
        menuret.append(C_menu("</li>","",""))
        menuret.append(C_menu("li","/structure/","Edificio"))
        menuret.append(C_menu("<ul>","",""))
        menuret.append(C_menu("li","javascript:;","Amenities"))
        menuret.append(C_menu("li","javascript:;","Resumen de expenas"))
        menuret.append(C_menu("li","javascript:;","Agenda"))
        
        menuret.append(C_menu("</ul>","",""))
        menuret.append(C_menu("li","javascript:;","Contacto"))
        menuret.append(C_menu("li","javascript:;","Mi Perfil"))
        menuret.append(C_menu("li","/logout","Log out"))
    else:
        menuret.append(C_menu("li","/accounts/login","Log In"))
    return menuret
  