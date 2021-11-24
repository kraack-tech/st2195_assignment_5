{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "825d40dd",
   "metadata": {},
   "outputs": [],
   "source": [
    "def is_divisible_by_k(x, k):\n",
    "'''\n",
    "Checks whether x is divisible by k.\n",
    "'''\n",
    "assert x%k == 0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "de87169f",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "Store all the integers that are multiples of 2 or 5 or 7 that are lower\n",
    "or equal to 1000 (excluding doubles)\n",
    "'''\n",
    "x = ()\n",
    "for i in range(1000):\n",
    "if (is_divisible_by_k(x, 2) & is_divisible_by_k(x, 3)) |\n",
    "is_divisible_by_k(x, 7):\n",
    "x.append(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2b62f7eb",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "Sum all the integers that are multiples of 2 or 5 or 7 that are lower\n",
    "or equal to 1000 (excluding doubles)\n",
    "'''\n",
    "sum(x)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
