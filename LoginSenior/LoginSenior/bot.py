from botcity.core import DesktopBot
from LoginSenior.credencials import Credencials

class Bot(DesktopBot):
    def action(self, execution=None):

# Open System the RH, Senior
        self.browse("https://emr-pontorh.whebdc.com.br/gestaoponto-frontend/login")

        # Screen the laptop
        """
        if not self.find( "User", matching=0.97, waiting_time=10000):
            self.not_found("User")
        self.click_relative(134, 8)
        """

        # Screen external of laptop
        if not self.find( "usuario", matching=0.97, waiting_time=10000):
            self.not_found("usuario")
        self.click()
        
        # Continuation of actions

        self.kb_type("SeuUsuário",2)

        self.tab()

        self.kb_type("SuaSenha",2)

        self.enter()

    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    Bot.main()










