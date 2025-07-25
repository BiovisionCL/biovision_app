
import 'package:flutter_test/flutter_test.dart';
import 'package:biovision_app/core/widgets/primary_button.dart';

void main() {
  testWidgets('PrimaryButton renders label', (WidgetTester tester) async {
    await tester.pumpWidget(
      PrimaryButton(label: 'Test', onPressed: () {}),
    );
    expect(find.text('Test'), findsOneWidget);
  });
}
