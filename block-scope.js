function scope() {
  if (true) {
    let inBlockLet = 2
    var inBlockVar = 3
    console.log(inBlockLet)
  }
  console.log(inBlockLet)
}

scope()
