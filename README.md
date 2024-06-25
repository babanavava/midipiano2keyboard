# midipiano2keyboard

MIDIピアノのキーボードの入力をPCの文字入力用のキーボードの入力に変換するプログラムを作ったのよ✨

## 使い方✨(windows限定✨)

1. [Releases](https://github.com/babanavava/midipiano2keyboard/releases/latest)から[**midipiano2keyboard-win.zip**](https://github.com/babanavava/midipiano2keyboard/releases/download/v0.0.0/midipiano2keyboard-win.zip)をダウンロードしてね✨

2. ファイルマネージャーを開きダウンロードした**midipiano2keyboard-win.zip**を選択し「**すべて展開**」を選択して、展開してね✨

3. 使用したいmidiデバイスを使うmidiソフトウェアが起動していないかを確認して、midiキーボードを接続してね✨

4. midipiano2keyboard-winフォルダ内の**midipiano2keyboard.exe**をダブルクリックして「**WindowsによってPCが保護されました**」と出た場合は[詳細情報](https://github.com/babanavava/midipiano2keyboard/releases)をクリックして、**実行**をクリックしてね✨

5. 現れたウィンドウの"Start"をクリックして、MIDIキーボードのC4あたりを適当に押してメモ帳などに文字が入力されるかを確認してね✨

**---------ここまででできればこれ以降は必要ないのよ✨---------**

6. もし入力されなければ midipiano2keyboard-winフォルダ内の**pygame_midi_device_detector.exe**を起動してね✨

7. 自分の使うMIDIデバイスと思しき名前のある行の、I/O列の**Input**とある行の左端のDevice IDとなる数字を覚えてね✨

(もし分からなければInputとあるDevice IDを総当たりしてみてね✨それと機器の接続をもう一度確認してね✨)

8. midipiano2keyboard-win内の**config.ini**をメモ帳などにドラッグアンドドロップしてね✨

9. `midi_input_device_id = 1`とあるところの`1`をさっき覚えたDevice IDに変えてね✨

10.  もう一度**ddj2key.exe**をダブルクリックして起動してね✨

11. これで文字入力がなされなければ、また`midi_input_device_id`の数字を適当に変えてみてね✨これで出来なければもう無理なのよ✨

## configsの説明✨

configsフォルダの中にプリセットとしてそれぞれキー配置の異なる4つのconfig.iniを作っておいたのよ✨

midipiano2keyboard.exeのあるフォルダのconfig.iniを上書きすればすぐに使うことが出来るのよ✨

それぞれどんな配置なのか説明するよ✨


### leverless
デフォルトの配置で、WASDが格ゲーのレバーレスコントローラーのように配置されている配置なのよ✨

元々このプログラムはスト6用のプログラムだからこれがデフォルトになっているのよ✨
![leverless](/configs/leverless(default)/leverless.png)

### keyboardy_WASD
**leverless**に比べてWASD部分が通常のキーボード風の配置となっていて、元々キーボードを使うゲームがやりやすそうな配置なのよ✨
![keyboardy_WASD](/configs/keyboardy_WASD/keyboardy_WASD.png)

### keyboardy_arrow
矢印キーを使ったゲームがやりやすそうな配置なのよ✨
![keyboardy_arrow](/configs/keyboardy_arrow/keyboardy_arrow.png)

### leverless_arrow
**leverless**のWASD部分を矢印キーに置き換えた配置なのよ✨
![leverless_arrow](/configs/leverless_arrow/leverless_arrow.png)

## config.iniの説明よ✨
上記のキー配置は全てconfig.iniの中に書かれてるから、それを自由に書き換えて君だけのオリジナル配置を作ることもできるのよ✨

### miscセクションの説明よ✨
- `midi_input_device_id`キーは、pygame.midiモジュールでのデバイスIDでどのデバイスを使用するかを決めるものなのよ✨(デフォルトは`1`よ✨)
- `octave_shift`キーは、`midi2key`セクションの各キーのオクターブ数に任意の値を足すことができるのよ✨(デフォルトは`0`よ✨)
- `transpose`キーは、`midi2key`セクションの割り当てを任意の値分だけ半音足すことができるのよ✨(デフォルトは`0`よ✨)
- `velocity_threshold`キーは、鍵盤を押す強さによって出力の有無を決めるしきい値を指定すことができるのよ✨ここを変えることはおすすめしないのよ✨(デフォルトは`0`で、`0-127`の範囲で指定できるのよ✨)
- `all_space`キーは`1`にするとこのプログラムで割り当て可能などのキーを押してもSPACEキーが入力されるようになるのよ✨(デフォルトは`0`よ✨)

### midi2keyセクションの説明よ✨
各キーが英語の音名とフラット`b`(小文字のB)とオクターブ数であらわされているのよ✨

念のため言っておくとC4がMIDIノートでいうところの60(10進数)に当たるのよ✨

config.iniにない範囲の音名も加えれば足せるから自由に割り当ててもいいのよ✨

## ライセンスよ✨
自由に使っていいのよ✨派生してもっといいアプリ作ってもらってもいいのよ✨

## クレジットよ！
- [pygame_midi_device_detector](https://github.com/babanavava/pygame_midi_device_detector) (https://github.com/babanavava/pygame_midi_device_detector)
