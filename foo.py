{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "621fbba0",
   "metadata": {},
   "source": [
    "## Practice assignment 5"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0dafd0d2",
   "metadata": {},
   "source": [
    "Checks whether x is divisible by k."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "7f032d85",
   "metadata": {},
   "outputs": [],
   "source": [
    "def is_divisible_by_k(x,k):\n",
    "  if(x%k==0):\n",
    "    print(\"Divisible\")\n",
    "  else:\n",
    "    print(\"Not divisible\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "f68e1625",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Divisible\n",
      "Not divisible\n"
     ]
    }
   ],
   "source": [
    "# test the function:\n",
    "is_divisible_by_k(10,2) # Should return \"Divisible\"\n",
    "is_divisible_by_k(37,2) # Should return \"Not divisible\""
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ef2aba9e",
   "metadata": {},
   "source": [
    "Store all the integers that are multiples of 2 or 5 or 7 that are lower or equal to 1000 (excluding doubles)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "70bc8513",
   "metadata": {},
   "outputs": [],
   "source": [
    "x = [x for x in range(1000) if x%2 == 0 or x%5 == 0 or x%7 == 0]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "eba91ba1",
   "metadata": {},
   "source": [
    "Sum all the integers that are multiples of 2 or 5 or 7 that are lower\n",
    "or equal to 1000 (excluding doubles)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "26b7ca2f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "327927"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
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
