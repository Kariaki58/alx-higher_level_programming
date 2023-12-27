#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    
    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")
    
    if len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")
    
    for vector in m_a:
        if type(vector) is not list:
            raise ValueError("m_a must be a list of lists")
    
    for vector in m_b:
        if type(vector) is not list:
            raise ValueError("m_b must be a list of lists")
    
    for vector in m_a:
        for data in vector:
            if type(data) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")
    
    for vector in m_b:
        for data in vector:
            if type(data) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")
            
    
    len_vector1 = len(m_a[0])
    len_vector2 = len(m_b[0])
    for vector in m_a:
        if len(vector) != len_vector1:
            raise TypeError("each row of m_a must be of the same size")
    
    for vector in m_b:
        if len(vector) != len_vector2:
            raise TypeError("each row of m_b must be of the same size")
    rows = len(m_b)
    for matrix in m_a:
        cols = len(matrix)
    if rows != cols:
        raise ValueError("m_a and m_b can't be multiplied")
    
    result = []
    print(rows)
    print(cols)