'''
Lost
作者：leonard
主程序
'''
import F_global as fg
import F_map as fm
from F_nature import build_nature
from F_player import buildplayer
from F_welcome import welcome

bo = True


class main(welcome):
    def main_menu(self):
        print('指令菜单:')
        for k, v in fg.menu.items():
            print(k, '.', v)

    def main_start(self, active, po, pp):
        bo = True
        if fg.menu.get(active, '请输入正确的菜单项') == '进入地图':
            yidong = '向%s移动(%s键),'
            yd = ''
            for k, v in fg.point_code.items():
                yd += yidong % (v, k)
            print('移动方式：', yd, '\n显示地图(i键),显示当前坐标值(o键),退出地图(q键)')
            map1 = fm.map()
            bo = map1.intomap(po, person)
        elif fg.menu.get(active, '请输入正确的菜单项') == '显示状态':
            bn = build_nature()
            bn.showuserinfo(pp)
        elif fg.menu.get(active, '请输入正确的菜单项') == '检查装备':
            pass
        elif fg.menu.get(active, '请输入正确的菜单项') == '存档':
            pass
        elif fg.menu.get(active, '请输入正确的菜单项') == '版本演化史':
            welcome.about(self)
        return bo


game = main()
active = 0

bp = buildplayer()
person = bp.create_player('s')
print('--------开始冒险---------')
while bo:
    game.main_menu()
    active = input()
    if not active:
        game.main_menu()
        continue
    if active.isalpha():
        game.main_menu()
        continue
    if int(active) not in fg.menu:
        game.main_menu()
        continue
    if active == '5':
        print('青山不改，绿水长流')
        break
    bo = game.main_start(int(active), fg.po, person)
if not bo:
    print('残念，END！')
