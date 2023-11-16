class CuentaBancaria:
    def __init__(self, saldo , titular):
        self._saldo = saldo
        self.titula = titular

    @property
    def saldo(self):
        return self._saldo

    def set_saldo(self,saldo):
        self._saldo = saldo    

    def depositar(self, monto):
        self._saldo = self._saldo + monto

    def retirar(self, monto):
        if self._saldo >= monto :
            self._saldo = self._saldo - monto 
            return monto 
        return 0         