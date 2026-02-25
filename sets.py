# 1st question
friday={"alice","bob","charlie"}
saturday ={"charlie","david","eve"}
all_guests=friday.union(saturday)
print("All Guests:",all_guests)
both_nights=friday.intersection(saturday)
print("Guest attendind both nights:",both_nights)

# 2nd question
data=[1,2,2,3,4,4,4,5]
unique_set=set(data)
unique_set.add(6)
print("Update set:",unique_set)

# 3rd question
library_books={"hobbit","1984","gatsby","odyssey","hamlet"}
checked_out={"1984","hamlet"}
available_book=library_books-checked_out
print("Availabel books:",available_book)
if "don quixote" not in library_books:
    library_books.add("don quixote")
    print("updated library:",library_books)

#4th question
user_permission={"read","write"}
admin_reqs={"read","write","execute"}
is_admin=user_permission.issubset(admin_reqs)
print("has admin access:",is_admin)
missing=admin_reqs-user_permission
print("Missing permission:",missing)

#5th question
logs={
    "404":[10,12,15,20],
    "500":[12,20,22,25],
    "403":[10,20,30]
}
all_errors_servers = set(logs["404"])&set(logs["500"])&set(logs["403"])
print("servers with all errors:",all_errors_servers)
critical_servers=set(logs["500"])-set(logs["404"])
print("Critical servers:",critical_servers)