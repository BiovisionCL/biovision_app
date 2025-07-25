
import 'package:flutter_test/flutter_test.dart';
import 'package:biovision_app/core/widgets/primary_button.dart';

void main() {
  testWidgets('PrimaryButton renders with given text', (WidgetTester tester) async {
    await tester.pumpWidget(
      PrimaryButton(text: 'Click Me', onPressed: () {}),
    );
    expect(find.text('Click Me'), findsOneWidget);
  });
}
