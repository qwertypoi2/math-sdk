import random
from config import PAYTABLE, REEL_STRIPS, PAYLINES, WILD

class SlotMachine:
    def __init__(self):
        self.reels = REEL_STRIPS
        self.paylines = PAYLINES
        self.paytable = PAYTABLE

    def spin_reels(self):
        board =[]
        for reel in self.reels:
            stop_idx = random.randint(0, len(reel) - 1)
            sym1 = reel[stop_idx]
            sym2 = reel[(stop_idx + 1) % len(reel)]
            sym3 = reel[(stop_idx + 2) % len(reel)]
            board.append([sym1, sym2, sym3])
        return board

    def evaluate_board(self, board):
        total_win = 0
        winning_lines =[]
        for line_idx, line in enumerate(self.paylines):
            line_symbols = [board[r][row] for r, row in enumerate(line)]
            first_symbol = line_symbols[0]
            target_symbol = first_symbol
            
            if first_symbol == WILD:
                for sym in line_symbols:
                    if sym != WILD:
                        target_symbol = sym
                        break
                        
            match_count = 0
            for sym in line_symbols:
                if sym == target_symbol or sym == WILD:
                    match_count += 1
                else:
                    break
                    
            if match_count >= 3:
                payout = self.paytable.get(target_symbol, {}).get(match_count, 0)
                if payout > 0:
                    total_win += payout
                    winning_lines.append({
                        "line": line_idx + 1,
                        "symbol": target_symbol,
                        "matches": match_count,
                        "payout": payout
                    })
        return total_win, winning_lines

    def play_round(self):
        board = self.spin_reels()
        total_win, winning_lines = self.evaluate_board(board)
        transposed = [[board[col][row] for col in range(5)] for row in range(3)]
        return {
            "board": transposed,
            "total_win": total_win,
            "winning_lines": winning_lines
        }
