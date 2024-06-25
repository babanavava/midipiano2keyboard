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
