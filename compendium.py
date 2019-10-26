import argparse, json, operator

class demon:
    def __init__(self, dict):
        vars(self).update(dict)

    def show(self):
        output = '{} {}'.format(self.race, self.name)
        if self.unique:
            output += ' (LIMITED)'
        output += '\n'

        output += '{:>4} {:<3} {:>4} {:<4} {:>3} {:<4}\n'\
                .format('LV', self.level, 'HP', self.HP, 'MP', self.MP)

        output += '{:>3} {:<3} {:>3} {:<3} {:>3} {:<3} {:>3} {:<3}\n'\
                .format('力', self.st, '魔', self.ma, '体', self.vi, '速', self.ag)

        output += '{:>3} {:<2} {:>3} {:<2} {:>3} {:<2}\n'\
                .format('物', self.phys, '火', self.fire, '氷', self.ice)

        output += '{:>3} {:<2} {:>3} {:<2} {:>3} {:<2}\n'\
                .format('電', self.elec, '衝', self.force, '魔', self.mystic)

        output += '  {}\n'.format('、 '.join(self.commands))

        output += '  {}\n'.format('、 '.join(self.passives))

        output += '  {}\n'.format(self.racial)

        print(output)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--race', help='filter by race (comma separated string)')
    parser.add_argument('-n', '--name', help='filter by name (comma separated string)')
    parser.add_argument('-l', '--list', help='number of results to display', type=int)
    parser.add_argument('-k', '--key', help='field to sort results by')
    parser.add_argument('-a', '--asc', help='display results in ascending order', action='store_true')
    args = parser.parse_args()

    with open('demons.json', 'r') as data:
        demons = json.loads(data.read(), object_hook=demon)

    args.key = args.key if args.key else 'level'
    args.sort = False if args.asc else True
    demons.sort(key=operator.attrgetter(args.key), reverse=args.sort)

    args.race = args.race.split('、') if args.race else None
    args.name = args.name.split('、') if args.name else None

    for demon in demons:
        if args.race and not demon.race in args.race:
            pass
        elif args.name and not demon.name in args.name:
            pass
        else:
            demon.show()
            if args.list:
                args.list -= 1
                if args.list <= 0:
                    break
