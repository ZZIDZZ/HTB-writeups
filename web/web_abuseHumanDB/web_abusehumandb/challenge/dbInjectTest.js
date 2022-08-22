var query = "SELECT * FROM userEntries WHERE title LIKE HTB" // AND approved = 1"
var query2 = "SELECT * FROM userEntries WHERE approved = ?" 


var injection = 'HTB UNION SELECT * FROM userEntries'

var injection2 = ""

console.log(query)

// or