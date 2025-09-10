def weight_converter(weight,unit):
    if unit=='kg':
        converted_weight=weight*2.2046
        return f"{converted_weght:.3f}pd"
    elif unit=='pd':
        converted_weight=weight/2.2046
        return f"{converted_weight:.3f}kg"
    else:
        return"输入单位错误，请输入'kg'或'pd'"
        
