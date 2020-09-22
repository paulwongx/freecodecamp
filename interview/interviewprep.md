# Legend
[Algorithms](#algorithms)
> [Symmetric Difference](##symmetric-difference)\
> [Merge Sort](##merge-sort)
[Definition of Terms](#definition-of-terms)

# Algorithms

## Symmetric Difference
```js
function sym(...args) { // linear time solution
	return [...args.reduce(reducer, new Set())];
}

const reducer = (result, arr) => {
	const compare = new Set(arr);
	for (let el of compare) result.has(el) ? result.delete(el) : result.add(el);
	return result;
}

sym([1, 2, 3], [5, 2, 1, 4], [4, 5, 6]); // [3, 6]
```

## Inventory Update
```js
function updateInventory(arr1, arr2) {
	let x;
	arr2.forEach(new=>{
		x=arr1.map(curr=>curr[1]).indexOf(new[1]); // check if new inv in existing inv
		(x==-1) ? arr1.push(e) : arr1[x][0]+=e[0]; // if new, add new inv, else add to existing inv
  	});
	return arr1.sort((a,b)=>(a[1]>b[1])?1:-1); // sort alphabetically
}

updateInventory([[1,'apple'],[5,'banana']], [[6,'apple'],[3,'milk']]);
```

## No Repeats
```js
function permAlone(str) {
  let regex = /(.)\1+/; // match repeated consecutive chars

  let arr=str.split(''); // split str to arr of ch
  let permutations=[], tmp;

  // Return 0 if str contains same character.
  if (str.match(regex) !== null && str.match(regex)[0] === str) return 0;

  const swap = (a, b) => { // swap placmeent
    tmp = arr[a];
    arr[a] = arr[b];
    arr[b] = tmp;
  }

  // Generate arrays of permutations using the algorithm.
  const generate = (int) => {
    if (int === 1) {
      // Make sure to join the characters as we create  the permutation arrays
      permutations.push(arr.join(""));
    } else {
      for (var i = 0; i != int; ++i) {
        generate(int - 1);
        swap(int % 2 ? 0 : i, int - 1);
      }
    }
  }

  generate(arr.length);

  // Filter the array of repeated permutations.
  let filtered = permutations.filter(function(string) {
    return !string.match(regex);
  });

  // Return how many have no repetitions.
  return filtered.length;
}

permAlone("aab"); // 2 since only [aba, aba] are unique
```

## [Pairwise](https://www.freecodecamp.org/forum/t/freecodecamp-challenge-guide-implement-bubble-sort/301612)
```js
function pairwise(arr, arg) {
  if (arr.length === 0) return 0;
  let pairs = [];
  for (let i = 0; i < arr.length; i++) {
    if (pairs.length === 0) {
      pairs.push([{value:arr[i], index:i}]);
    } else {
      for (let j = 0; j < pairs.length; j++) {
        if (pairs[j][0].value === arg - arr[i] && pairs[j].length===1) {
          pairs[j].push({value:arr[i], index:i});
          break;
        } else if (j === pairs.length - 1) {
            pairs.push([{value:arr[i], index:i}]);
            break;
          }
      }
    }
  }
  console.log(pairs);
  pairs = pairs.filter(e => e.length === 2).map(e => e[0].index+e[1].index);
  console.log(pairs);
  let re = pairs.reduce((a, b) => a + b);
  console.log(re);
  return re;
}

pairwise([1,4,2,3,0,5], 7);
```

## Bubble Sort
```js
// Compare element with one ahead of it. O(n^2) complexity
function bubbleSort(arr) {
  for (let i=0; i<arr.length; i++) {
    for (let j=0; j<arr.length-1-i; j++) {
      if (arr[j] > arr[j+1])
        [arr[j],arr[j+1]] = [arr[j+1],arr[j]]; // Using ES6 array destructuring to swap
    }
  }
  return arr;
}

bubbleSort([1, 4, 2, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92]);
```

## Selection Sort
```js
function swap(a, b, arr) {
  let tmp = arr[a];
  arr[a] = arr[b];
  arr[b] = tmp;
}
function selectionSort(array) {
  for (let i = 0; i < array.length - 1; i++) {
    let min = i;
    for (let j = i + 1; j < array.length; j++) {
      if (array[min] > array[j]) min = j;
    }
    swap(i, min, array);
  }
  return array;
}

selectionSort([1, 4, 2, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92]);
```

## Insertion Sort
```js
function insertionSort(array) {
  for (let i = 1; i < array.length; i++) {
    let curr = array[i];
    for (var j = i - 1; j >= 0 && array[j] > curr; j--) {
      array[j + 1] = array[j];
    }
    array[j + 1] = curr;
  }
  return array;
}

insertionSort([1, 4, 2, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92]);
```

## Quick Sort
```js
//Swapping array elements via ES6 array destructuring
function swap(arr, x, y) {
  [arr[x], arr[y]] = [arr[y], arr[x]];
}

//Pivot function returns the fixed pivot point
function pivot(arr, left = 0, right = arr.length - 1) {
  let shift = left;
  for (let i = left + 1; i <= right; i++) {
    //Move all the small elements on the left side
    if (arr[i] < arr[left]) swap(arr, i, ++shift);
  }

  //Finally swapping the last element with the left
  swap(arr, left, shift);
  return shift;
}

function quickSort(array, left = 0, right = array.length - 1) {
  if (left < right) {
    let pivotIndex = pivot(array, left, right);

    //Recusrively calling the function to the left of the pivot and to the right of the pivot
    quickSort(array, left, pivotIndex - 1);
    quickSort(array, pivotIndex + 1, right);
  }
  return array;
}

quickSort([1, 4, 2, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92]);
```

## Merge Sort
```js
function merger(arr1, arr2) {
  let i = 0,
    j = 0,
    mergedArr = [];
  while (i < arr1.length && j < arr2.length) {
    if (arr1[i] > arr2[j]) mergedArr.push(arr2[j++]);
    else mergedArr.push(arr1[i++]);
  }
  while (i < arr1.length) {
    mergedArr.push(arr1[i++]);
  }
  while (j < arr2.length) {
    mergedArr.push(arr2[j++]);
  }
  return mergedArr;
}
function mergeSort(array) {
  //Array of length 1 is sorted so we return the same array back
  if (array.length == 1) return array;

  //Break down the array to half from middle into left and right
  let middle = Math.floor(array.length / 2);
  let left = mergeSort(array.slice(0, middle));
  let right = mergeSort(array.slice(middle));

  //Return the merged sorted array
  return merger(left, right);
}

mergeSort([1, 4, 2, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92]);
```

# Definition of Terms
* [Permutation](mathsisfun.com/combinatorics/combinations-permutations.html) - Order *does* matter (to rmbr: **P**ermutation... **P**osition)
	1. Repetition allowed: n^r
		* A 3 code(r) locker with 10 numbers(n), has 10x10x10 = 1,000 permutations
	2. Repetition not allowed: n!/(n-r)! = P(n,r) = nPr
		* Choosing 3 balls(r) out of 16 pool balls(n), has 16x15x14 = 3,360 permutations
* [Combination](mathsisfun.com/combinatorics/combinations-permutations.html) - Order doesn't matter
	1. Repetition allowed (scoops of icecream flavors): C(r+n-1,r) = C(r+n-1,n-1) = (r+n-1)!/r!(n-1)!
		* Reformulated to choose r flavors from r+(n-1) positions
	2. Repetition not allowed (lottery numbers): n!/r!(n-r)! = C(n,r) = (n,r) = nCr = n choose r = Binomial Coefficient
		* Permutation without repetition reduced by # of ways it could be in order = /r!
		* C(n,r) same as C(n, n-r) - Choosing 3 balls out of 16, same as choosing 13 balls out of 16
