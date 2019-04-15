from sys import argv

script, argu1, argu2 = argv
prompt='>'

print(f'The running script is {script}, user is {argu1}, object is {argu2}')

print(f'{argu2}, do you like games ?', end=' ')
ans=input(prompt)

print(f'{argu2}, what game do you like?', end=' ')
game=input(prompt)

print(f'''From the diology between {argu1} and {argu2}
{argu2} likes {game}
{script} end''')
