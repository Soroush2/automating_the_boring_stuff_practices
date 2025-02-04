def isValidChessBoard(board):
    #valid positions
    validPositions={str(r)+c for r in range(1,9) for c in 'abcdefgh'}
    #valid pieces name
    valid_piece={'pawn','knight','bishop','rook','queen','king'}
    #valid count tracker
    piece_counter={'w':{'total':0,'king':0,'pawn':0},'b':{'total':0,'king':0,'pawn':0,'bishop':0,'knight':0,'queen':0}}
    for position,piece in board.items():
        if position not in validPositions:
            print('invalid position')
            return False
        if piece[1:] not in valid_piece or piece[0] not in 'wb':
            print('invalid format')
            return False
        
        color=piece[:1]
        piece_counter[color]['total']+=1
        piece_type=piece[1:]
        if piece_type=='king':
            piece_counter[color]['king']+=1
        elif piece_type=='pawn':
            piece_counter[color]['pawn']+=1
        if piece_counter[color]['total']>16 or piece_counter[color]['pawn'] > 8:
            print('Invalid number of pawns or tatal pieces')
            return False
    if piece_counter['w']['king']==1 and piece_counter['b']['king']==1:
        return True
    else:
        print(f"number of kings is not valid: whiteKings: {piece_counter['w']['king']} BlackKings: {piece_counter['b']['king']}")
        return False 
        





    