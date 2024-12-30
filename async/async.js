
// Create  a Promise
const p=Promise((resolve,reject) => {
    const numberOfCustomers=10;
    if (numberOfCustomers > 5) {
        resolve("OK")
    }
    else {
        reject(" Not enough promotion")
    }
})
p.then((data)=>{console.log(data);}).catch((error)=>{console.log(error);})
p.then((value )=>{console.log(value);}).catch((reason)=>{console.log(reason);})
// when you do request to the server you will receive a Promise you will get it in json format;
// method1: of consuming a Promise
p.then( value => {
    console.log(value)
}).catch(
    (error)=> {
        console.log(error)
    }
)
p.then((value)=>{
    console.log(value);
}).catch((error)=>{
    console.log(error);
})
//method2: of consuming a Promise;
const value=await p; 
// you can just use it with async functions or use top level await there certain conditions for that

const checkResults = async () => {
    const value = await p ;
    console.log(value);
}
//  what if the Promise returns an error ?

const checkResultsNew = async () => {
    try { 
    const value = await p ;
    console.log(value);
}
catch (reason) {
    console.log(reason);
}
}

// why & where use promises
// majority of your code is synchronous 
// const a = 1 ; 
// const b= 2 ;
// const c = 3 ;

// this is no problem because these operations are very fast

// however , some operations may take a long time 
// (and we don't want to freeze our program)
// we want to use asynchronous code for them

//  on front-end : Network requests (Fetch API , axios library)
// on back-end : interacting with file system 
