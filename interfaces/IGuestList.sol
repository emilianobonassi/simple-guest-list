// SPDX-License-Identifier: AGPL-3.0
// Feel free to change the license, but this is what we use

pragma solidity 0.6.12;

interface IGuestList {
    function authorized(address guest, uint256 amount) external view returns (bool);
}