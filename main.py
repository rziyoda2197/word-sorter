def sozlar_alfavitga_saralash(sozlar):
    return sorted(sozlar)

sozlar = ["apple", "banana", "cherry", "date", "elderberry"]
print(sozlar_alfavitga_saralash(sozlar))
```

```python
def sozlar_alfavitga_saralash(sozlar):
    return sorted(sozlar, key=str.lower)

sozlar = ["Apple", "banana", "Cherry", "date", "Elderberry"]
print(sozlar_alfavitga_saralash(sozlar))
```

```python
def sozlar_alfavitga_saralash(sozlar):
    return sorted(sozlar, key=lambda x: x.lower())

sozlar = ["Apple", "banana", "Cherry", "date", "Elderberry"]
print(sozlar_alfavitga_saralash(sozlar))
