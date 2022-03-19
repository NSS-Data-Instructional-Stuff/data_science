import matplotlib.pyplot as plt

def find_zip(sample, zips):
    for zipcode in zips:
        if sample[zipcode] == 1:
            return zipcode.split('_')[1]
        
def get_zip_coef(sample, zips, coefficients):
    idx = sample.index.to_list().index(f'zipcode_{find_zip(sample, zips)}')
    return coefficients[idx]

def tell_me_why(linreg, sample, column_names):
    '''
    This will generate a plot showing why a linear regression model made the predictions that it did.
    It currently only works specifically for the King County housing data.
    
    parameters:
    	linreg: A (fit) linear regression model.
    	sample: A single instance for which you want an explanation of linreg's prediction.
    	column_names: The predictor column names in the correct order
    '''

    plt.figure(figsize = (14, 10))

    nonzip = [colname for colname in column_names if 'zipcode' not in colname]
    zips = [colname for colname in column_names if 'zipcode' in colname]

    plt.ylim(0, 21)
    plt.xlim(-1, 3)

    fontsize = 18

    plt.annotate(xy = (1.5, 20), text = 'coefficient', fontsize = fontsize, ha = 'right', fontweight = 'bold')
    plt.annotate(xy = (3, 20), text = 'value', fontsize = fontsize, ha = 'right', fontweight = 'bold')

    for i,colname in enumerate(nonzip):
        plt.annotate(xy = (0, 19 - i), text = colname + ':', fontsize = fontsize, ha = 'right')
        plt.annotate(xy = (0.5, 19-i), text = sample[colname], fontsize = fontsize, ha = 'right')
        plt.annotate(xy = (1.5, 19-i), text = "{:,.0f}".format(round(linreg.coef_[i], 0)), fontsize = fontsize, ha = 'right')
        plt.annotate(xy = (3, 19-i), text = "{:,.0f}".format(round(sample[colname] * linreg.coef_[i], 0)), fontsize = fontsize, ha = 'right')
        
        plt.plot([-1,3], [19 - i - 0.2, 19 - i - 0.2], linewidth = 0.5, color = 'grey')


    plt.annotate(xy = (0, 2), text = 'zipcode:', fontsize = fontsize, ha = 'right')
    plt.annotate(xy = (0.5, 2), text = find_zip(sample, zips), fontsize = fontsize, ha = 'right')
    plt.annotate(xy = (1.5, 2), text = "{:,.0f}".format(round(get_zip_coef(sample, zips, linreg.coef_), 0)), fontsize = fontsize, ha = 'right')
    plt.annotate(xy = (3, 2), text = "{:,.0f}".format(round(get_zip_coef(sample, zips, linreg.coef_), 0)), fontsize = fontsize, ha = 'right')
    plt.plot([-1,3], [2 - 0.2, 2 - 0.2], linewidth = 0.5, color = 'grey')

    plt.annotate(xy = (0, 1), text = 'intercept:', fontsize = fontsize, ha = 'right')
    plt.annotate(xy = (3, 1), text = "{:,.0f}".format(round(linreg.intercept_, 0)), fontsize = fontsize, ha = 'right')

    plt.annotate(xy = (1.5, 0), text = 'Prediction:', fontsize = fontsize, ha = 'right', fontweight = 'bold',
                color = 'red')

    plt.plot([2,3], [0.9,0.9], linewidth = 3, color = 'black')

    plt.annotate(xy = (3, 0), text = "${:,.0f}".format(round(linreg.predict(sample.values.reshape(1,-1))[0], 0)), fontsize = fontsize, ha = 'right', fontweight = 'bold',
                color = 'red')

    plt.axis('off');
