/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let value=init
    return{
     increment:()=>{
        value+=1;
        return value
    },
     reset:()=>{
        value=init;
        return value
    },
     decrement:()=>{
        value-=1;
        return value
    }
    }
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */