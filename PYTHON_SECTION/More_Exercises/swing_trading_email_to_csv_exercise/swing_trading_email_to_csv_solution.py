"""
Scenario:
    - Your client has a subscription to a swing trading newsletter.
    - Every week the client gets an email with list of trades.
    - the client tracks their trades in a spreadsheet and every week they have to copy the
        trades from the email into their tracking spreadsheet.
    - The client wants a script that will parse the text from the email and create a csv
      so it is easy to copy all trades into the tracking list

Exercise
    * Create a program that will output a file with a list of trades listed in the email body.
    * The output file should have the following columns
    symbol,trade_type,entry_price,stop_loss_price,target_price

Hint/Suggestion:
    * first create a dictionary with all the trades. each trade is a dictionary and all dictionaries are in a list.
    * use the dictionary to create the file
"""

import pdb
import pprint

result_file_path = "/Volumes/GoogleDrive/My Drive/PROJECTS/SuperSQA/Courses/MegaCourses/SeleniumPython/course-code/course-code-py-selenium-video/course-selenium-and-python/PYTHON_SECTION/More_Exercises/swing_trading_email_to_csv_exercise/output.csv"
all_trades_raw = """
PEP Short $153.68
Stop Loss $156.98
Target $146.10

LIN Short $309.97
Stop Loss $315.82
Target $282.00

REGN Short $644.64
Stop Loss $659.77
Target $539.00

ORI Short $24.84
Stop Loss $25.60
Target $22.90

DELL Short $94.16
Stop Loss $97.19
Target $90.00

AXP Short $156.80
Stop Loss $162.16
Target $148.00

TEAM Short $377.31
Stop Loss $387.49
Target $343.00

PANW Short $463.73
Stop Loss $479.01
Target $400

HLI Short $88.19
Stop Loss $91.49
Target $75.00

BR Short $168.49
Stop Loss $172.86
Target $158.00

ZTS Short $205.45
Stop Loss $210.11
Target $176.00

LSI Short $125.18
Stop Loss $129.88
Target $98.00

CYRN Long $0.6200
Stop Loss $0.5000
Target $0.8100
"""

def raw_string_to_dictionary(input_string):

    input_as_list = input_string.split('\n\n')

    all_trades = []
    for trade in input_as_list:
        trade_split = trade.split()
        symbol = trade_split[0]
        trade_type = trade_split[1]
        entry_price = trade_split[2]
        stop_loss_price = trade_split[5]
        target = trade_split[7]

        trade_dictionary = {
            'symbol': symbol,
            'trade_type': trade_type,
            'entry_price': entry_price,
            'stop_loss_price': stop_loss_price,
            'target': target
        }
        all_trades.append(trade_dictionary)

    print(all_trades)
    pprint.pprint(all_trades)

    # pdb.set_trace()
def raw_string_to_dictionary_v2(input_string): # same thing as the previous function but cleaner code

    input_as_list = input_string.split('\n\n')

    all_trades = []
    for trade in input_as_list:
        trade_split = trade.split()
        trade_dictionary = {
            'symbol': trade_split[0],
            'trade_type': trade_split[1],
            'entry_price': trade_split[2],
            'stop_loss_price': trade_split[5],
            'target': trade_split[7]
        }
        all_trades.append(trade_dictionary)

    return all_trades

def create_trades_file(output_path, trades):
    """

    :param output_path: expect a full path of the file to be created.
    :param trades:
    :return:
    """

    with open(output_path, 'w') as f:
        f.write("symbol,trade_type,entry_price,stop_loss_price,target_price\n")
        for i in trades:
            f.write(f"{i['symbol']},{i['trade_type']},{i['entry_price']},{i['stop_loss_price']},{i['target']}\n")


### start of function calls
all_trades_formatted = raw_string_to_dictionary_v2(all_trades_raw)
pprint.pprint(all_trades_formatted)

create_trades_file(result_file_path, all_trades_formatted)