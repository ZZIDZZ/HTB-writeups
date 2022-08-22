let smt = await this.db.prepare('SELECT username FROM users WHERE username = \'admin\' and password = \'\'')

// \" OR \"1\"=\"1

// clue: SSRF SQL injection