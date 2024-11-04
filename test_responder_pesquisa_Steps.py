from lib2to3.fixes.fix_next import bind_warning

from pytest_bdd import given, when, then, scenarios
from playwright.sync_api import expect, Page
from credencial_linkedin import email, senha

scenarios('../feature/responder_pesquisa.feature')


@given("que esteja na pesquisa escolhida")
def acessar_pesquisa(browser: Page):
    browser.goto('https://forms.office.com/Pages/ResponsePage.aspx?id=DQSIkWdsW0yxEjajBLZtr'
                 'QAAAAAAAAAAAAYAAMaaJIFUNzBRVzVKMVFSVTdaSU5KM0E3OEQ2MlZWNS4u')


@when("faco o preenchimento das perguntas")
def responder_pesquisa_de_forma_automatica(browser: Page):
   browser.get_by_text('Sim', exact=True).click()
   browser.locator('[placeholder="Insira sua resposta"]').fill('Essa pesquisa está sendo respondida de forma'
                                                               'automatizada')
   browser.locator('[aria-label="9 Heart"]').click()


@then("devo enviar as respostas, fazer a validacao e depois responder novamente")
def enviar_respostas_e_fazer_a_validacao_depois_responder_novamente(browser: Page):
  for _ in range(4):
   browser.get_by_text('Enviar',exact=True).click()
   expect(browser.get_by_text('Sua resposta foi enviada', exact=True))
   browser.get_by_text('Enviar outra resposta', exact=True).click()

   browser.get_by_text('Sim', exact=True).click()
   browser.locator('[placeholder="Insira sua resposta"]').fill('Essa pesquisa está sendo respondida de forma'
                                                               'automatizada')
   browser.locator('[aria-label="9 Heart"]').click()




