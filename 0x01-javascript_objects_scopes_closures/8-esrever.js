#!/usr/bin/node
exports.esrever = function (list) {
    let j = list.length - 1;
    const revlist = [];
    for (let i = 0; i < list.length; i++) {
      revlist[i] = list[j];
      j--;
    }
    return revlist;
  };
