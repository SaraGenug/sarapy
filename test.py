season = ['Spring', 'Summer', 'Fall', 'Winter']
iter_season = iter(season)
print(type(iter_season)) # 型を表示して確認

print(next(iter_season)) # 1番目のイテレータを表示後、次のイテレータに進む

# イテレータを１つずつ取り出して表示
for i in iter_season:
    print(i)