# Álcool, açúcares e bits: Aprendizado de Máquina e a química dos vinhos

___Projeto desenvolvido para a VI FECIB 2017___

___1º colocado na categoria Projeto Didático EM___

__Orientador:__ <a href="http://lattes.cnpq.br/3995585094514614" target="_blank">Prof. Rafael José de Alencar Almeida</a><br />
__Coorientador:__ <a href="http://lattes.cnpq.br/4539575610533576" target="_blank">Luciano Carlos de Paiva</a>

__Alunos do Curso Técnico em Química__:
- Nícolas de Freitas Amaral
- Pedro Henrique Oliveira da Silva
- Thiago Henrique Reis<br />

<img src="http://aprendizadodemaquina.com.br/wine1.png">

_O presente trabalho tem como objetivo apresentar de forma didática o que é o Aprendizado de Máquina, suas aplicações nas mais diversas áreas do conhecimento e seus impactos na sociedade moderna. Será demonstrado um exemplo prático de aprendizado de máquina contextualizado em relação à química dos vinhos, ilustrando como a Química está presente no cotidiano, e como redes neurais artificiais podem ser aplicadas em diversos domínios de problemas. Pretende-se estimular os visitantes a construírem um novo olhar sobre como a tecnologia, aliada às áreas tradicionais do conhecimento, possibilita a construção de novas realidades e possibilidades, pautadas na inovação e na multidisciplinaridade._

<img src="http://aprendizadodemaquina.com.br/wine2.png">

## Instalação e configuração 
<p>Caso ainda não tenha, instale a versão do Python3 disponível em https://www.python.org/downloads, de acordo com sua distribuição.</p> 
<p>Vamos utilizar o <a href=https://virtualenv.pypa.io/en/stable/>Virtualenv</a>, onde será possível a instalação de todas as depêndencias, utilizadas no programa, em um ambiente virtual. No linux, em distribuições baseada no Debian,  o Virtualenv pode ser instalado com comando:</p>
<pre>$ sudo apt-get install virtualenv</pre>

Clone ou baixe este repositório e descompacte na pasta:
<pre>$ git clone https://github.com/rafjaa/machine_learning_fecib.git </pre>

Entre na pasta do projeto e crie um ambiente virtual com Virtualenv, especificando a versão utilizada do Python:
<pre>$ virtualenv qlv --python=python3</pre>

Após a criação é necessário ativar o ambiente, o mesmo pode ser realizado com o comando:
<pre>$ source qlv/bin/activate</pre>

Com o ambiente virtual ativado, instale as dependências, listadas no arquivo "requirements.txt":
<pre>(qlv)$ pip install -r requirements.txt</pre>

Com o ambiente configurado, entre na pasta "/src" e execute o arquivo "server.py". Após, abra o navegador e vá para o endereço: http://127.0.0.1:5000:
<pre>(qlv)$ python server.py</pre>

